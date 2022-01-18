var path = require("path");
const fs = require("fs");

const targetSource = "./build";
const targetDestination = "../static";

/**
 * Remove directory recursively
 * @param {string} dir_path
 */

function rimraf(dir_path) {
    if (fs.existsSync(dir_path)) {
        fs.readdirSync(dir_path).forEach(function(entry) {
            var entry_path = path.join(dir_path, entry);
            if (fs.lstatSync(entry_path).isDirectory()) {
                rimraf(entry_path);
            } else {
                fs.unlinkSync(entry_path);
            }
        });
        fs.rmdirSync(dir_path);
    }
}


/**
 * Copy a file
 * @param {string} source
 * @param {string} target
 */

function copyFileSync(source, target) {
    var targetFile = target;
    // if target is a directory a new file with thw same will be created.
    if (fs.existsSync(target)) {
        if (fs.lstatSync(target).isDirectory()) {
            targetFile = path.join(target, path.basename(source));
        }
    }
    fs.writeFileSync(targetFile, fs.readFileSync(source));
}


/**
 * Copy a folder recursively
 * @param {string} source
 * @param {string} target
 */

function copyFolderRecursiveSync(source, target, root=false) {
    var files = [];
    var targetFolder = root ? target : path.join(target, path.basename(source));
    if (!fs.existsSync(targetFolder)) {
        fs.mkdirSync(targetFolder);
    }

    if (fs.lstatSync(source).isDirectory()) {
        files = fs.readdirSync(source);
        files.forEach(function (file) {
            var curSource = path.join(source, file);
            if (fs.lstatSync(curSource).isDirectory()) {
                copyFolderRecursiveSync(curSource, targetFolder);
            } else {
                copyFileSync(curSource, targetFolder);
            }
        });
    }
}

//Caculate absolute paths using the relative paths we defined at the top
const sourceFolder = path.resolve(targetSource);
const destinationFolder = path.resolve(targetDestination);


// Remove destination folder if it exists to clear it.
if (fs.existsSync(destinationFolder)) {
    rimraf(destinationFolder)
}

// Copy the build over
copyFolderRecursiveSync(sourceFolder, destinationFolder, true)