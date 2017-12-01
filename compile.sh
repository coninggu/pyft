#!/usr/bin/env bash
java -jar closure-compiler/closure-compiler-v20171112.jar --compilation_level SIMPLE_OPTIMIZATIONS --js pyft/static/pyft.js --js_output_file pyft/static/pyft-min.js