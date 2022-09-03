#!/bin/bash

# local-vars: 演示本地变量脚本

foo=0 # global variable foo

funct_1 () {
  local foo # funct_1 局部变量foo
  foo=1
  echo "funct_1: foo = $foo"
  return
}

funct_2 () {
  local foo # funct_2局部变量foo
  foo=2
  echo "funct_2: foo = $foo"
  return
}

echo "global: foo = $foo"
funct_1
echo "global: foo = $foo"
funct_2
echo "global: foo = $foo"