---
layout: page
title: Projects
permalink: /projects/
---
In this page, I will showcase my finished projects.


#### Modeling Vesicle Budding Dynamics

<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

<div class="center-image">
  <img id="gif-image" src="{{ '/images/projects/budded_state.png' | relative_url }}" class="responsive-image-abstract" alt="Abstract Image">
  <p>Click the image to play/pause video</p>
</div>

<script>
  $(document).ready(function(){
    $("#gif-image").click(function(){
      // Toggle between the GIF and the static image
      var currentSrc = $(this).attr("src");
      if(currentSrc.includes("movie_budding.gif")) {
        $(this).attr("src", "{{ '/images/projects/budded_state.png' | relative_url }}"); // Pause (static image)
      } else {
        $(this).attr("src", "{{ '/images/projects/movie_budding.gif' | relative_url }}"); // Play (GIF)
      }
    });
  });
</script>

- **Description:** Explored the budding mechanism of lipid nanoscale vesicles under physiological conditions using a detailed continuum elastic model. The study focused on high-curvature transitions and revealed that lipid demixing reduces energy barriers for budding. This research highlights the role of asymmetry in leaflet composition, osmotic balance, and area, identifying lipid domain formation as a key driver of significant curvature changes.

- **Significance:** Results provide insights into biological processes like viral budding and endocytosis, showcasing the importance of lipid sorting and heterogeneity in regulating vesicle dynamics.

- **Preprint:** [here](https://doi.org/10.1101/2024.10.24.620077).

#### The Two Faces of the Lo Phase

<div class="center-image">
  <img src="https://pubs.acs.org/cms/10.1021/acs.jpclett.1c03712/asset/images/medium/jz1c03712_0005.gif"  class="responsive-image-abstract"  alt="Abstract Image">
</div>

- **Description:** Investigated the structural characteristics of the liquid-ordered (L<sub>o</sub>) lipid phase in model membranes through molecular simulations. Identified and characterized small, mostly hexagonally packed lipid clusters within the L<sub>o</sub> phase, which are rigid in room temperature. These clusters undergo melting upon heating, and notably, this transition occurs in proximity to physiological conditions, suggesting its potential biophysiological significance.

- **Publication:** [here](https://pubs.acs.org/doi/full/10.1021/acs.jpclett.1c03712).


#### Lipid Nanodiscs Elasticity

<div class="center-image">
  <img src="https://pubs.acs.org/cms/10.1021/acs.jctc.2c01054/asset/images/medium/ct2c01054_0005.gif"  class="responsive-image-abstract"  alt="Abstract Image">
</div>

- **Initial Study:** Through molecular simulations and continuum elastic theory, I've investigated the elastic properties of lipid nanodiscs, nanometric bilayer patches enveloped by membrane scaffolding proteins (MSPs). Employed a computational approach, based on molecular dynamics simulations, to quantify bending rigidity (K<sub>C</sub>) and tilt modulus (κ<sub>t</sub>) locally. Results revealed that nanodiscs exhibit unique material properties compared to infinite bilayers of corresponding lipid composition, showing higher stiffness and spatial variations in moduli.

- **Follow-up study:**
  - I've used a continuum elastic theory to understand the interplay between MSP geometry, lipid confinement, and nanodisc shape.
  - The equilibrium nanodisc shape was determined by minimizing the elastic free energy functional, providing a quantitative understanding of nanodisc deformations.
  - The results demonstrated sensitivity of the nanodisc shape to its size, lipid density, and lipid tilt and thickness at the MSP contact.
  - The bending rigidity was novely extracted from the membrane shape profile by fitting the numerically minimized full elastic functional to said profile.

- **Significance:** Findings show the importance of considering nanodisc deformations and material properties when interpreting both structure and function of proteins embedded within nanodiscs. The integration of a continuum elastic theory offers a comprehensive understanding of the relationship between nanodisc structure and membrane material properties.

- **Publications:** [here](https://pubs.acs.org/doi/full/10.1021/acs.jctc.2c01054) and [here](https://pubs.acs.org/doi/10.1021/acs.jpcb.0c03374).


#### "Simplifying" Glass Transition (for BSc. Hon. Thesis)

<div class="center-image">
  <img src="{{ '/images/projects/amirim_proj.png' | relative_url }}" class="responsive-image-abstract" alt="Abstract Image">
</div>
<div class="center-image">
  <img src="{{ '/images/projects/amirim_proj2.png' | relative_url }}"  class="responsive-image-abstract"  alt="Abstract Image">
</div>

- **Description:** Investigated the glass transition in anisotropic systems through constant pressure Monte Carlo simulations, with advanced simulation methods such as Replica Exchange - all coded from scratch. Focused on finding simple potentials which result in glass transition and understanding the interplay of kinetic and thermodynamic factors.

- **Significance:** Demonstrated that a single-component system comprising point particles with anisotropic "quasi-dipole" interactions undergoes a glass transition when the interaction strength is sufficiently high. This observation could have implications for applications in materials science.

- **Resulting thesis:** [here](https://raw.githubusercontent.com/infinityScha/blog/master/files/projects/amirim%20work.pdf).
