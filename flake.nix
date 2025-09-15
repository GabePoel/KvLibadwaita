{
  description = ''
    KvLibadwaita theme for Kvantum which repeats
    the Libadwaita design for your QT applications
    The gradience feature provides the ability
    to override the theme color scheme.
    35 presets from popular themes in
    base16 format are available to choose from
    If your favorite color scheme is not in the list,
    you can pass the path to the base16.json file
    with your favorite theme in base16 format to the builder
  '';

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }: let
    supportedSystems = [
      "x86_64-linux"
      "x86_64-darwin"
      "aarch64-linux"
      "aarch64-darwin"
    ];
    forAllSystems = nixpkgs.lib.genAttrs supportedSystems;
    nixpkgsFor = forAllSystems (system: import nixpkgs { inherit system; });
in {
  # Executed by `nix build .#<name>`
  packages = forAllSystems (system: let
      pkgs = nixpkgsFor.${system};
  in rec {
    kvlibadwaita = pkgs.callPackage ./nix/kvlibadwaita.nix {};
    default = kvlibadwaita;
  });
  overlays = (import ./nix/overlays.nix { })
  // { default = self.overlays.kvlibadwaita ; };
  homeManagerModules.kvlibadwaita = import ./nix/module.nix;
  homeManagerModule = self.homeManagerModules.kvlibadwaita;
  };
}
