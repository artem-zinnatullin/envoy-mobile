licenses(["notice"])  # Apache 2

load("//bazel:aar_with_jni.bzl", "aar_with_jni")
load("//bazel:kotlin_lib.bzl", "envoy_mobile_kt_aar_android_library", "envoy_mobile_kt_library")

aar_with_jni(
    name = "android_aar",
    android_library = "envoy_lib",
    archive_name = "envoy",
    visibility = ["//visibility:public"],
)

envoy_mobile_kt_aar_android_library(
    name = "envoy_lib",
    srcs = [
        "Envoy.kt",
    ],
    custom_package = "io.envoyproxy.envoymobile",
    manifest = "EnvoyManifest.xml",
    visibility = ["//visibility:public"],
    deps = ["//library/java/io/envoyproxy/envoymobile/engine:envoy_engine_lib"],
)

envoy_mobile_kt_library(
    name = "envoy_interfaces_lib",
    srcs = [
        "Client.kt",
        "EnvoyException.kt",
        "Request.kt",
        "RequestBuilder.kt",
        "RequestMethod.kt",
        "ResponseHandler.kt",
        "RetryPolicy.kt",
        "StreamEmitter.kt",
    ],
    visibility = ["//visibility:public"],
)
