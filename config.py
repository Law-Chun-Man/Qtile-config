from subprocess import call
from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy

mod = "mod4"
HOME = "/home/(your user name)"
wallpaper_path = f"{HOME}/your wallpaper path"
browser = "firefox-esr"
terminal = "xfce4-terminal --disable-server"

COLOUR = {
    "grey": "777777",
    "cyan": "00eeff",
    "black": "000000",
}

@hook.subscribe.startup_once
def autostart():
    qtile.groups_map["0"].cmd_toscreen()                    # Go to workspace 10 on startup
    call(f"{HOME}/.config/qtile/bash_script/autostart.sh")  # run startup script

keys = [
    # Monitor
    Key([], "XF86Display", lazy.spawn(f'{terminal} -e "{HOME}/.config/qtile/bash_script/monitor.sh"'), desc="Change monitor"),
    # Screenshot
    Key([], "Print", lazy.spawn("bash -c 'xfce4-screenshooter -crs Pictures/screenshots/screenshot_$(date +\%Y\%m\%d_\%H\%M\%S).png'"), desc="screenshot area"),
    Key([mod], "Print", lazy.spawn("bash -c 'xfce4-screenshooter -cfs Pictures/screenshots/screenshot_$(date +\%Y\%m\%d_\%H\%M\%S).png'"), desc="screenshot area"),
    # Clipboard manager
    Key([mod], "v", lazy.spawn("xfce4-popup-clipman"), desc="clipboard manager"),
    # Play-pause
    Key(["mod1"], "space", lazy.spawn("playerctl play-pause"), desc="Play pause"),
    # Volume control
    Key([], "XF86AudioLowerVolume", lazy.spawn(f"{HOME}/.config/qtile/dunst/volume_decrease.sh"), desc="Decrease volume"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(f"{HOME}/.config/qtile/dunst/volume_increase.sh"), desc="Increase volume"),
    Key([], "XF86AudioMute", lazy.spawn(f"{HOME}/.config/qtile/dunst/volume_mute.sh"), desc="Toggle mute"),
    Key([], "XF86AudioMicMute", lazy.spawn(f"{HOME}/.config/qtile/dunst/mic_mute.sh"), desc="Toggle mute mic"),
    # Brightness control
    Key([], "XF86MonBrightnessUp", lazy.spawn(f"{HOME}/.config/qtile/dunst/brightness_increase.sh"), desc="Increase brighness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn(f"{HOME}/.config/qtile/dunst/brightness_decrease.sh"), desc="Decrease brighness"),
    # Poweroff
    Key(["control", "mod1"], "delete", lazy.spawn("sudo poweroff"), desc="Poweroff"),

    # Launcher
    Key([mod], "slash", lazy.spawn("xfce4-appfinder -c"), desc="Launch appfinder"),
    Key([mod, "shift"], "XF86Touchpadoff", lazy.spawn(f"xfce4-appfinder"), desc="Launch appfinder"),
    Key([mod], "p", lazy.spawn(f"xfce4-appfinder"), desc="Launch appfinder"),
    Key(["control", "mod1"], "f", lazy.spawn(browser), desc="Launch Firefox"),
    Key(["control", "mod1"], "t", lazy.spawn(terminal), desc="Launch terminal"),
    Key(["control", "mod1"], "k", lazy.spawn("kdeconnect-app"), desc="Launch kdeconnect"),
    Key(["control", "mod1"], "h", lazy.spawn("thunar"), desc="Launch file explorer"),
    Key(["control", "mod1"], "y", lazy.spawn(f'{browser} --private-window "youtube.com"'), desc="Open youtube on private tab"),
    Key(["control", "mod1"], "p", lazy.spawn(f"{HOME}/.local/share/JetBrains/Toolbox/apps/pycharm-community/bin/pycharm.sh"), desc="Launch pycharm"),
    Key(["control", "mod1"], "w", lazy.spawn(f"{HOME}/.local/share/JetBrains/Toolbox/apps/webstorm/bin/webstorm.sh"), desc="Launch webstorm"),

    # Switch between windows
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "m", lazy.layout.swap_main(), desc="Move focus to main"),
    # Swap windows
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Resize windows.
    Key([mod], "h", lazy.layout.shrink_main(), desc="Shrink main"),
    Key([mod], "l", lazy.layout.grow_main(), desc="Grow main"),
    Key([mod, "control"], "j", lazy.layout.grow(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.shrink(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.reset(), desc="Reset all window sizes"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"], "w", lazy.spawn("dm-tool lock"), desc="Lock screen"),
    #Key([mod], "Return", lazy.spawncmd(command="bash -ic '%s'"), desc="Spawn a command with aliases in bashrc enabled."),

    # Scratchpad
    Key([], "XF86Favorites", lazy.group['scratchpad'].dropdown_toggle('calc'), desc="Bring up calculator scratchpad"),
    Key(["control", "mod1"], "c", lazy.group['scratchpad'].dropdown_toggle('calc'), desc="For keyboard without calculator key"),
    Key([mod], "semicolon", lazy.group['scratchpad'].dropdown_toggle('file'), desc="Bring up file manager"),
    Key([mod], "Return", lazy.group['scratchpad'].dropdown_toggle('terminal'), desc="Bring up terminal"),
    Key(["control", "mod1"], "v", lazy.group['scratchpad'].dropdown_toggle('vpn'), desc="Bring up vpn"),
]

group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
group_labels = ["➊", "➋", "➌", "➍", "➎", "➏", "➐", "➑", "➒", "➓"]
groups = [Group(name=group_names[i], label=group_labels[i]) for i in range(10)]

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
            # mod + control + group number = switch to & move focused window to group
            Key(
                [mod, "control"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc=f"Move focused window to group {i.name}",
            ),
        ]
    )

# Add scratchpads
groups += [
    ScratchPad("scratchpad", [
        DropDown("file", "thunar", height=0.5, y=0.2, width=0.7, x=0.15, opacity=1),
        DropDown("terminal", terminal, height=0.5, y=0.25, width=0.5, x=0.25, opacity=1),
        DropDown("volume", "pavucontrol", height=0.5, y=0.2, width=0.4, x=0.3, opacity=1),
    ]),
]

layouts = [
    layout.MonadTall(
        border_focus=COLOUR["cyan"],
        border_normal=COLOUR["black"],
        change_ratio=0.03,
        single_border_width=0,
        new_client_position='top',
        max_ratio=0.85,
        min_ratio=0.15
    ),
    layout.Max(),
]

widget_defaults = dict(
    font="URW Gothic Bold",
    fontsize=20,
    padding=0,
)

screens = [
    Screen(
        wallpaper = wallpaper_path,
        wallpaper_mode='fill',
        top=bar.Bar(
            [
                # Left
                # Mode switcher
                widget.Image(
                    filename=f"{HOME}/.config/qtile/widget_icons/weather-storm.svg",
                    mouse_callbacks = {'Button1': lazy.spawn(f'{HOME}/.config/qtile/dunst/mode_switcher.sh')},
                    margin_x=3,
                    margin_y=1
                ),
                widget.TextBox(fmt="  "),


                # Layout icon
                widget.CurrentLayoutIcon(margin_x=3, margin_y=1),
                widget.TextBox(fmt="  "),


                # Show workspace
                widget.GroupBox(
                    fontsize=22,
                    highlight_method='text',
                    use_mouse_wheel=False,
                    inactive=COLOUR["grey"],
                    margin_x=2,
                    margin_y=2,
                    this_current_screen_border=COLOUR["cyan"]
                ),
                widget.TextBox(fmt="  "),


                widget.Spacer(),


                # Right
                widget.Systray(icon_size=22),
                widget.TextBox('   '),


                # Memory
                widget.Image(
                    filename=f"{HOME}/.config/qtile/widget_icons/disk-utility.png",
                    margin_y=1
                ),
                widget.TextBox(' '),
                widget.GenPollCommand(cmd=f"{HOME}/.config/qtile/bash_script/mem.sh", update_interval=2),
                widget.TextBox('   '),


                # Network
                widget.Image(
                    filename=f"{HOME}/.config/qtile/widget_icons/network-wireless.png",
                    margin_y=1
                ),
                widget.TextBox(' '),
                widget.GenPollCommand(cmd=f"{HOME}/.config/qtile/bash_script/internet.sh", update_interval=2),
                widget.TextBox('   '),


                # CPU Temperature
                widget.Image(
                    filename=f"{HOME}/.config/qtile/widget_icons/utilities-system-monitor.svg",
                    margin_y=1
                ),
                widget.TextBox(' '),
                widget.GenPollCommand(cmd=f"{HOME}/.config/qtile/bash_script/cpu_temp.sh", update_interval=2),
                widget.TextBox('   '),


                # Volume
                widget.Image(
                    filename=f"{HOME}/.config/qtile/widget_icons/audio-volume-high.svg",
                    mouse_callbacks = {'Button1': lazy.group['scratchpad'].dropdown_toggle('volume')},
                    margin_y=1
                ),
                widget.Volume(
                        fmt=' {}   ',
                        mouse_callbacks={'Button1': lazy.group['scratchpad'].dropdown_toggle('volume'), 'Button2': None, 'Button3': None, 'Button4': None, 'Button5': None}
                ),


                # Battery
                widget.BatteryIcon(
                    theme_path=f"{HOME}/.config/qtile/battery_icons",
                    scale=1.1
                ),
                widget.GenPollCommand(cmd=f"{HOME}/.config/qtile/bash_script/bat.sh", update_interval=60),
                widget.TextBox('   '),


                # Date
                widget.GenPollCommand(cmd=f"{HOME}/.config/qtile/bash_script/date.sh", update_interval=86400),
                widget.TextBox('  '),
                widget.GenPollCommand(cmd=f"{HOME}/.config/qtile/bash_script/time.sh", update_interval=1),
                widget.TextBox(' '),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = False
bring_front_click = True
floats_kept_above = True
cursor_warp = False

# Float rules
floating_layout = layout.Floating(
    border_width = 2,
    border_focus = COLOUR["cyan"],
    border_normal = COLOUR["grey"],
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='blueman-manager'),
        Match(wm_class='xfce4-appfinder'),
    ]
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"

