# This Repository is Unmaintained

The EAF JS Video Player is currently not supported, please use the [EAF Video Player](https://github.com/emacs-eaf/eaf-video-player) instead.

# EAF Video Player (JS)
This repository provides the EAF Video Player (JS) application for the [Emacs Application Framework](https://github.com/emacs-eaf/emacs-application-framework).

### Load application
[Install EAF](https://github.com/emacs-eaf/emacs-application-framework#install) first, then add below code in your emacs config:

```Elisp
(add-to-list 'load-path "~/.emacs.d/site-lisp/emacs-application-framework/")
(require 'eaf)
(require 'eaf-js-video-player)
```

### The keybinding of EAF JS Video Player.

| Key   | Event   |
| :---- | :------ |
| `x` | close_buffer |
| `f` | toggle_fullscreen |
| `M-g` | exit_fullscreen |
| `<f12>` | open_devtools |
| `SPC` | js_toggle_play |
| `h` | js_backward |
| `l` | js_forward |
| `r` | js_restart |
| `j` | js_decrease_volume |
| `k` | js_increase_volume |
| `c--` | zoom_out |
| `C-=` | zoom_in |
| `C-0` | zoom_reset |
