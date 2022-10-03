#!/bin/bash
install_ansible() {
  # install ansible on local machine
  if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    sudo apt-get update
    sudo apt-get install ansible
  elif [[ "$OSTYPE" == "darwin"* ]]; then
    brew install ansible
  else
    echo "unrecognized os. Exiting"
  fi
}

if ! command -v ansible &> /dev/null ; then
    install_ansible
fi
