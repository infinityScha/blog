---
layout: post
title: How to Paint a Periodic Zebra? (in Python)
---

The first time (and certainly not the last) I was required to paint a periodic zebra was for a spatial analysis of a molecular simulation during my master. In this post, I will show you a cool trick, using the beautiful mathematical concept of permutation parity, for striped domains segragation under periodic boundary conditions (all explained below!).
<div class="center-image">
  <img src="{{ '/images/periodic_zebra/periodic_zebra.jpg' | relative_url }}"  class="responsive-image"  alt="Abstract Image">
</div>

First of all, **WHY IS THIS IMPORTANT?** We will get into the technical importance later. But ideologically, I think that this exercise is an excellent example of a compact and elegant analysis using a seemingly unrelated piece of math. I believe that a broad understanding of mathematics (as well as other displines) and keeping an open mind are highly beneficial for efficient and elegant problem solving.

## So what is a periodic zebra?

As a physicist in training, I must obivously approximate my zebra as a rectangle with wiggly black-white stripes over it.

<div class="center-image">
  <img src="{{ '/images/periodic_zebra/zebra_approx.jpg' | relative_url }}"  class="responsive-image"  alt="Abstract Image">
</div>

But this is still a standard (?) zebra, nothing periodic about it. We can now make it periodic by demanding the stripes to follow a periodic pattern in both $x$ and $y$ directions. Meaning that our rectangle (middle boxes in the illustration below) serves as a unit cell from which we can build periodic images by translation.

<div class="center-image">
  <img src="{{ '/images/periodic_zebra/periodic_zebra_ex.jpg' | relative_url }}"  class="responsive-image"  alt="Abstract Image">
</div>

and thus, we have defined a periodic zebra!

### Why you should care about periodic zebras

The ideological importance of this exercise was already given in the beginning of this post. Practically, you should care about it if you work with simulations in general or with periodic data, signals or images. Most molecular and a significant portion of other numerical simulations are running under what is termed **periodic boundary conditions** (**PBC**). This means that the system is assumed to be periodic (particles feel each other and can pass from one side of the box to the other) and thus it only requires running simulation of the unit cell. While PBC has many benefits (such as making the computational cost feasible while mostly avoiding unnatural artifacts) it is usually more annoying to analyse such simulations as particles "teleport" between box sides. 

I specifically painted periodic zebras for analyzing molecular simulations that contain two coexisting phases (usually organised as stripes in the simulation box). Painting zebras was specifically useful for finding which molecule resides in each phase or calculating the overall area of each phase, after I initially identified the boundaries between the two phases.

## Guided tour

### Statement of the problem

We have a periodic rectangle with a point cloud scattered over it. We are also provided with an even number, $2k$, of periodic lines, each termed $l_i$, defining the interfaces between the zebra strips. Why $2k$? because a periodic zebra must have $2n$ interfaces between the strips! (try to make one with an uneven number of interfaces and see what you get)

insert image

Each line is required to be not *too wiggly*. In more rigorous terms, we demand that the lines are uniquely defined as a function of $y$, meaning that the line does not cross any line $y=c$ more than once. Therefore, we can define $l_i(y)$ as the $x$ coordinate of the $i$th line at height $y$. Furthermore, we would request that the lines won't cross each other and that no point in the point cloud falls EXACTLY on a line (otherwise they are an interfacial point which should not be black nor white).

insert image

Our mission is to color the point cloud in accordance to the stripe, black or white, it belongs to.

insert image

The first piece of code will create, for simplicity, a gridded version of the cloud scatter and the priodic lines:


```python
import numpy as np
import matplotlib.pyplot as plt

# Set the random seed for reproducibility
np.random.seed(42)

# Define the grid size
N, M = 20, 10

# Generate random points over the grid
points = np.random.choice([0, 1], size=(N, M))

# Define 4 periodic lines
x = np.linspace(0, N-1, N)
line1 = (np.sin(x) + 1) * (M-1) / 2
line2 = (np.cos(x) + 1) * (M-1) / 2
line3 = (np.sin(x + np.pi/4) + 1) * (M-1) / 2
line4 = (np.cos(x + np.pi/4) + 1) * (M-1) / 2

# Plot the grid and the periodic lines
plt.figure(figsize=(8, 8))
plt.imshow(points, cmap='Greys', interpolation='none', extent=[0, N-1, 0, M-1])
plt.plot(x, line1, label='Line 1', color='red')
plt.plot(x, line2, label='Line 2', color='blue')
plt.plot(x, line3, label='Line 3', color='green')
plt.plot(x, line4, label='Line 4', color='purple')
plt.legend()
plt.title('Periodic Lines and Random Points on Grid')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()
```

add code here + plot.

In order to solve this problem *elegantly* we will use the concept of **permutation's parity**.


### Brief introduction to permutations

We first need to briefly define what is a **tuple** (in mathematics). A set is, for our purposes, a "group" of numbers, this numbers do not have any defined order within the set. For example, a specific set, which we would name $S$ of the numbers $1,2,3$ is presented by $S=${$1,2,3$} and due to the lack of order, it can be presented by {$2,1,3$} or {$3,1,2$}. On the other hand, tuple is an ordered list of numbers, we will represent it as $(a,b,c,d...)$ where $a$ is the first number, $b$ is the second and so on. As an example, $(1,2,3)$ is a tuple which is <u>not</u> equal to $(2,1,3)$.

insert image

A **permutation** of $S$ is an ordered list, containing each number from $S$ exactly once. The set {$1,2,3$} has exactly six different permutations: $(1,2,3)$, $(2,3,1)$, $(3,2,1)$, $(1,3,2)$, $(2,1,3)$ and $(3,1,2)$. We will now limit ourself to the set {$1,2,\cdots,n$}. The The "naive" tuple: $(1,2,\cdots,n)$ is termed as the **identity permutation**. As any number, the total number of flips between 2 elements of the permutation required to get from some permutation to the identity permutation is either **even** or **odd**. By this number of flips, a permutation is characterized as either even or odd. This characterization is termed the permutation **parity**. This dichotomic relation would be the basis which by we will paint our periodic zebra.

insert image

### So how can we paint the periodic zebra with it?

For each point $(a,b)$ in the point cloud, we will do the following procedure: (illustrated below)
- we would define the following identity permutation $(1,2,\cdots,2k,2k+1)$. We say that the index $i<2k+1$ corresponds to $l_i$, while the last index which corresponds to the point.
- we would number between the $2k$ interfaces and the point by their $x$ coordinates ($l_i(b)$ for the interfaces and $a$ for the point) from left to right (or right to left, doesn't matter, just be consistent).

  We call this number the *location* of index $i$ and is marked by $n_i$. By our requirements (not too wiggley lines, etc) we ensure that the location is unique for each line and the point and goes from $1$ to $2k+1$ (it can be said that the location *maps* the identity permutation).

- next, we would form a permutation with the locations (lets call it the **location permutation**), $(n_1,n_2,\cdots,n_{2k},n_{2k+1})$. Then, we have to find the parity of this permutation (SciPy got us covered).
- the parity value corresponds to the fitting color for the point. We would assume that even corresponds to white and odd corresponds to black.

insert image

The following script does exactly that:

insert code + result
```python
import numpy as np
from scipy.linalg import lu

# Example code to find the parity of a permutation
def find_parity(permutation):
    _, _, p = lu(np.array(permutation))
    return np.sum(p) % 2

# Example usage
permutation = [3, 1, 2]
parity = find_parity(permutation)
print("Parity:", "even" if parity == 0 else "odd")
```


### Why does it work??

Because for $2k+1$-permutations (such as the location permutation), <u>the parity is conserved under translation in PBC</u>. It is visually proven below for $3$:

insert image

For $2k$-permutation the parity is switched when a point crosses to the other side of the box. 

## Concluding remarks

In this blog post I've presented a useful (for some) way to segragate points under PBC using the concept of permutation parity. This is not a common practice and I suspect that the main reason is that most people who deal with molecular simulations (such as computational chemists/biologists and some physists) are not familiar with this concept. Although this is not the whole deal, as I stated in the beginning, mathematical prowess can come useful in my programmatical tasks and in my opinion should be always kept in mind. However, this advice is probably not limited to mathematics as other disiplines have some tricks up their sleeves that may prove useful as well.