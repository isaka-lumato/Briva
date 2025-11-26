// Project data will be loaded from JSON file
let projectData = null;

// Function to get URL parameter
function getUrlParameter(name) {
  name = name.replace(/[\[]/, '\\[').replace(/[\]]/, '\\]');
  const regex = new RegExp('[\\?&]' + name + '=([^&#]*)');
  const results = regex.exec(location.search);
  return results === null ? '' : decodeURIComponent(results[1].replace(/\+/g, ' '));
}

// Function to load project data from JSON
async function loadProjectData() {
  try {
    const response = await fetch('data/projects.json');
    if (!response.ok) {
      throw new Error('Failed to load project data');
    }
    projectData = await response.json();
    return projectData;
  } catch (error) {
    console.error('Error loading project data:', error);
    return null;
  }
}

// Function to update page content
function updatePageContent(project) {
  // Update page title
  document.title = `Briva - ${project.title} | Project Details`;

  // Update banner title
  const bannerTitle = document.querySelector('.banner-title');
  if (bannerTitle) {
    bannerTitle.textContent = project.title;
  }

  // Update breadcrumb
  const breadcrumbActive = document.querySelector('.breadcrumb-item.active');
  if (breadcrumbActive) {
    breadcrumbActive.textContent = project.title;
  }

  // Update meta description
  const metaDescription = document.querySelector('meta[name="description"]');
  if (metaDescription) {
    metaDescription.setAttribute('content', project.description);
  }

  // Update project images in slider
  const pageSlider = document.getElementById('page-slider');
  if (pageSlider) {
    // Check if slick is already initialized and destroy it
    if (typeof $.fn.slick !== 'undefined' && $(pageSlider).hasClass('slick-initialized')) {
      $(pageSlider).slick('unslick');
    }

    pageSlider.innerHTML = '';
    project.images.forEach(imagePath => {
      const sliderItem = document.createElement('div');
      sliderItem.className = 'item';
      sliderItem.innerHTML = `<img loading="lazy" class="img-fluid" src="${imagePath}" alt="${project.title}" />`;
      pageSlider.appendChild(sliderItem);
    });

    // Reinitialize slick slider if it exists
    if (typeof $.fn.slick !== 'undefined') {
      setTimeout(() => {
        $(pageSlider).slick({
          fade: true,
          slidesToShow: 1,
          slidesToScroll: 1,
          autoplay: true,
          autoplaySpeed: 5000,
          dots: false,
          speed: 600,
          arrows: true,
          prevArrow: '<button type="button" class="carousel-control left" aria-label="carousel-control"><i class="fas fa-chevron-left"></i></button>',
          nextArrow: '<button type="button" class="carousel-control right" aria-label="carousel-control"><i class="fas fa-chevron-right"></i></button>'
        });
      }, 100);
    }
  }

  // Update project title in content
  const columnTitle = document.querySelector('.column-title');
  if (columnTitle) {
    columnTitle.textContent = project.title;
  }

  // Update project description
  const descriptionParagraph = document.querySelector('.column-title + p');
  if (descriptionParagraph) {
    descriptionParagraph.textContent = project.description;
  }

  // Update project info
  const projectInfoItems = document.querySelectorAll('.project-info li');
  if (projectInfoItems.length >= 5) {
    // Client
    const clientContent = projectInfoItems[0].querySelector('.project-info-content');
    if (clientContent) clientContent.textContent = project.client;

    // Location
    const locationContent = projectInfoItems[1].querySelector('.project-info-content');
    if (locationContent) locationContent.textContent = project.location;

    // Size
    const sizeContent = projectInfoItems[2].querySelector('.project-info-content');
    if (sizeContent) sizeContent.textContent = project.size;

    // Year
    const yearContent = projectInfoItems[3].querySelector('.project-info-content');
    if (yearContent) yearContent.textContent = project.year;

    // Categories
    const categoriesContent = projectInfoItems[4].querySelector('.project-info-content');
    if (categoriesContent) categoriesContent.textContent = project.categories;
  }
}

// Function to load project details
async function loadProjectDetails() {
  // Load project data from JSON
  const data = await loadProjectData();

  if (!data) {
    console.error('Failed to load project data');
    return;
  }

  const projectId = getUrlParameter('project');

  if (!projectId || !data[projectId]) {
    // If no valid project ID, use core-drilling as default
    const defaultProject = data['core-drilling'] || data[Object.keys(data)[0]];
    updatePageContent(defaultProject);
    return;
  }

  const project = data[projectId];
  updatePageContent(project);
}

// Load project details when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', loadProjectDetails);
} else {
  loadProjectDetails();
}
