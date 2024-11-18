module.exports.readVersion = function (contents) {
  const match = contents.match(/version\s*=\s*"([^"]+)"/)
  return match ? match[1] : '0.0.0'
}

module.exports.writeVersion = function (contents, version) {
  return contents.replace(
    /version\s*=\s*"[^"]+"/,
    `version = "${version}"`
  )
}
