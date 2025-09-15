# █░█ █▀▄▀█ ▄▄ █▀▄▀█ █▀█ █▀▄ █░█ █░░ █▀▀ ▀
# █▀█ █░▀░█ ░░ █░▀░█ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄
# -- -- -- -- -- -- -- -- -- -- -- -- -- -

{ config, pkgs, lib, ... }: let
  cfg = config.qt.kvlibadwaita;
  kvlibadwaita = pkgs.callPackage ./kvlibadwaita.nix {
    theme = cfg.theme;
    base16-scheme-path = cfg.base16-scheme-path;
  };
  in {
  options.qt.kvlibadwaita = with lib; {
    enable = mkEnableOption "Enable KvLibadwaita";
    theme = mkOption {
      type = types.str;
      default = "adwaita";
      description = ''
        Preset name.
        If the value is missing or equal to adwaita,
        the default theme will be installed
        If the value is custom, the builder expects
        the base16-scheme-path option; 
        if it is not specified, the catppuccin_mocha theme will be built.
      '';
    };
    base16-scheme-path = mkOption {
      type = types.pathInStore;
      default = ../gradience/base16/catppuccin_mocha.json;
      description = ''
        Path to your own base16 theme in /nix/store
        The file is expected to be in json format.
        The file must repeat the structure of any of the presets.
      '';
    };
    auto = mkOption {
      type = types.bool;
      default = true;
      description = ''
        If true KvLibadwaita will be installed as default theme
        You will not be able to change
        the file ~/.config/Kvantum/kvantum.kvconfig from kvantummanager
        Set to false if you want to manually change kvantummanager settings
      '';
    };
  };
  config = with pkgs; with lib; mkIf cfg.enable {
    home.packages = [
      libsForQt5.qtstyleplugin-kvantum
      qt6Packages.qtstyleplugin-kvantum
      kvlibadwaita
    ];
    xdg.configFile = {
      "Kvantum/KvLibadwaita".source = "${kvlibadwaita}/share/Kvantum/KvLibadwaita";
    } // (
      if cfg.auto then {
        "Kvantum/kvantum.kvconfig".text = ''
          [General]
          theme=KvLibadwaita
        '';
      } 
      else {}
    );
  };
}
