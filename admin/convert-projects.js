// Convert projects.json from object-based to array-based format for Decap CMS
const fs = require('fs');
const path = require('path');

const projectsPath = path.join(__dirname, '..', 'data', 'projects.json');
const projectsBackupPath = path.join(__dirname, '..', 'data', 'projects-backup.json');

// Read current projects
let currentProjects;
try {
    currentProjects = JSON.parse(fs.readFileSync(projectsPath, 'utf8'));
} catch (error) {
    console.error('❌ Error reading projects.json:', error.message);
    process.exit(1);
}

// Check if already in Decap format
if (currentProjects.projects && Array.isArray(currentProjects.projects)) {
    console.log('ℹ️  Projects are already in Decap CMS format');

    // Validate the array format
    const firstProject = currentProjects.projects[0];
    if (firstProject && firstProject.id) {
        console.log('✅ Format is correct - no conversion needed');
        process.exit(0);
    }
}

// Backup current format (only if not already backed up)
if (!fs.existsSync(projectsBackupPath)) {
    fs.writeFileSync(projectsBackupPath, JSON.stringify(currentProjects, null, 2));
    console.log('✅ Backup created: projects-backup.json');
} else {
    console.log('ℹ️  Backup already exists, skipping...');
}

// Convert from object to array format
let projectsArray = [];

// If it's the old object format
if (!currentProjects.projects) {
    projectsArray = Object.entries(currentProjects).map(([id, project]) => ({
        id: id,
        ...project
    }));
} else {
    // It's wrapped but might be malformed
    console.log('⚠️  Attempting to fix malformed format...');

    // Try to extract from nested structure
    const wrapped = currentProjects.projects;
    if (Array.isArray(wrapped) && wrapped.length > 0) {
        // Check if it's nested objects
        const first = wrapped[0];
        if (typeof first === 'object' && !first.id) {
            // Extract all nested projects
            wrapped.forEach(item => {
                Object.values(item).forEach(project => {
                    if (project.id) {
                        projectsArray.push(project);
                    }
                });
            });
        }
    }
}

if (projectsArray.length === 0) {
    console.error('❌ No valid projects found to convert');
    process.exit(1);
}

// Wrap in the format Decap expects
const decapFormat = {
    projects: projectsArray
};

// Save new format
fs.writeFileSync(projectsPath, JSON.stringify(decapFormat, null, 2));
console.log(`✅ Converted ${projectsArray.length} projects to Decap CMS format`);
console.log('✅ projects.json updated successfully');
