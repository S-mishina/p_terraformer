#!/bin/bash
function help(){
    echo "Usage: ./setup.sh -e <Operation System>" 1>&2
    echo "ex)" 1>&2
    echo "./setup.sh -e Darwin" 1>&2
    exit 1
}
while [ ${#} -gt 0 ]
    do
        case $1 in
        '-h'|'--help' )
            help
            ;;
        '-e' )
            if [ -z "$2" ]; then
            help
            else
                Operation="$2"
                shift 2
            fi
            ;;
      esac
    done
if [ -z "$Operation" ]; then
    help
    exit 0
fi
if [[ "$Operation" == "Darwin" ]] || [[ "$Operation" == "Linux" ]]; then
    curl -LO https://github.com/GoogleCloudPlatform/terraformer/releases/download/$(curl -s https://api.github.com/repos/GoogleCloudPlatform/terraformer/releases/latest | grep tag_name | cut -d '"' -f 4)/terraformer-all-"$Operation"-amd64
    chmod +x terraformer-all-"$Operation"-amd64
    sudo mv terraformer-all-"$Operation"-amd64 /usr/local/bin/terraformer
else
    echo "no support terraformer"
fi
