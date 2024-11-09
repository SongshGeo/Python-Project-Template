const stringifyPackage = require('stringify-package')
const detectIndent = require('detect-indent')
const detectNewline = require('detect-newline')

module.exports.readVersion = function (contents) {
  const match = contents.match(/version\s*=\s*"([^"]+)"/)
  return match ? match[1] : '0.0.0'
}

module.exports.writeVersion = function (contents, version) {
  const indent = detectIndent(contents).indent
  const newline = detectNewline(contents)
  return contents.replace(
    /version\s*=\s*"[^"]+"/,
    `version = "${version}"`
  )
}
