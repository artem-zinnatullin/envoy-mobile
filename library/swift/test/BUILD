licenses(["notice"])  # Apache 2

load("@envoy//bazel:envoy_build_system.bzl", "envoy_package")
load("@build_bazel_rules_apple//apple:ios.bzl", "ios_unit_test")
load("@build_bazel_rules_swift//swift:swift.bzl", "swift_library")

envoy_package()

swift_library(
    name = "testlib",
    srcs = [
        "SampleTest.swift",
    ],
    deps = [
        "//library/swift/src:ios_framework_archive",
    ],
)

ios_unit_test(
    name = "sample_test",
    minimum_os_version = "11.0",
    deps = [":testlib"],
)
