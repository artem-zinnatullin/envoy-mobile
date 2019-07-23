load("@io_bazel_rules_kotlin//kotlin:kotlin.bzl", "kt_jvm_test")

# A basic macro to make it easier to declare and run kotlin tests
#
# Ergonomic improvements include:
# 1. Avoiding the need to declare the test_class which requires a fully qualified class name (example below)
# 2. Avoiding the need to redeclare common unit testing dependencies like JUnit
# 3. Ability to run more than one test file per target
#
# Usage example:
# load("//bazel:kotlin_test.bzl", "envoy_mobile_kt_test)
#
# envoy_mobile_kt_test(
#     name = "example_kotlin_test",
#     srcs = [
#         "ExampleTest.kt",
#     ],
# )
#
def envoy_mobile_kt_test(name, srcs, deps = []):

    # This is to work around the issue where we have specific implementation functionality which
    # we want to avoid comsumers to use but we want to unit test
    dep_srcs = []
    for dep in deps:
        dep_srcs.append(dep+"_srcs")

    kt_jvm_test(
        name = name,
        test_class = "io.envoyproxy.envoymobile.bazel.EnvoyMobileTestSuite",
        srcs = srcs + dep_srcs,
        deps = [
            "//bazel:envoy_mobile_test_suite",
            "@maven//:org_assertj_assertj_core",
            "@maven//:junit_junit",
        ],
    )
