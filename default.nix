{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  name = "eletromidia-env";
  nativeBuildInputs = with pkgs.buildPackages; [
    python312 
    poetry 
    pkg-config 
    gcc-unwrapped
  ];

  shellHook = ''
    alias p='poetry run'
    alias pt='poetry run task'
    alias pm='p python manage.py'

    if [ -f .env.nix ]; then
      export $(grep -v '^#' .env.nix | xargs)
    fi

    export LD_LIBRARY_PATH=${pkgs.lib.makeLibraryPath [
      pkgs.stdenv.cc.cc
    ]}
    
  '';
}
