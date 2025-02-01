from os.path import expanduser
import subprocess
from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy

mod = "mod4"
HOME = expanduser("~")
wallpaper_path = "sports-car-futuristic-mountain-sunset-scenery-digital-art-4k-wallpaper-uhdpaper.com-537@0@i.jpg"
browser = "firefox-esr"
terminal = "kitty"

COLOUR = {
    "grey": "777777",
    "cyan": "00ffff",
    "magenta": "ff00ff",
    "white": "ffffff",
    "red": "ff0000",
    "green": "00ff00"
}

# Go to workspace 10 on startup
@hook.subscribe.startup_once
def start_on_workspace_10():
    qtile.groups_map["0"].cmd_toscreen()

# run startup script
@hook.subscribe.startup_once
def autostart():
    subprocess.call(f"{HOME}/.config/qtile/autostart.sh")

# later set mod+d to show desktop
@lazy.function
def minimise_all(qtile):
    for win in qtile.current_group.windows:
        if hasattr(win, "toggle_minimize"):
            win.toggle_minimize()

keys = [
    #Screenshot
    Key([mod, "shift"], "s", lazy.spawn("bash -c 'xfce4-screenshooter -crs Pictures/screenshots/screenshot_$(date +\%Y\%m\%d_\%H\%M\%S).png'"), desc="screenshot area"),
    Key([], "Print", lazy.spawn("bash -c 'xfce4-screenshooter -cfs Pictures/screenshots/screenshot_$(date +\%Y\%m\%d_\%H\%M\%S).png'"), desc="screenshot fullscreen"),
    # Clipboard manager
    Key([mod], "v", lazy.spawn("xfce4-popup-clipman"), desc="clipboard manager"),
    # Play-pause
    Key(["mod1"], "space", lazy.spawn("playerctl play-pause"), desc="Play pause"),
    # Volume control
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"), desc="Decrease volume"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"), desc="Increase volume"),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"), desc="Toggle mute"),
    Key([], "XF86AudioMicMute", lazy.spawn("pactl set-source-mute @DEFAULT_SOURCE@ toggle"), desc="Toggle mute mic"),
    # Brightness control
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +2%"), desc="Increase brighness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 2%-"), desc="Decrease brighness"),
    #Poweroff
    Key(["control", "mod1"], "delete", lazy.spawn("sudo poweroff"), desc="Poweroff"),

    #Launcher
    Key([mod], "slash", lazy.spawn("xfce4-appfinder -c"), desc="Launch appfinder"),
    Key(["control", "mod1"], "f", lazy.spawn(browser), desc="Launch Firefox"),
    Key(["control", "mod1"], "t", lazy.spawn(terminal), desc="Launch terminal"),
    Key(["control", "mod1"], "k", lazy.spawn("kdeconnect-app"), desc="Launch kdeconnect"),
    Key(["control", "mod1"], "h", lazy.spawn("thunar"), desc="Launch file explorer"),
    Key(["control", "mod1"], "y", lazy.spawn(f'{browser} --private-window "youtube.com"'), desc="Open youtube on private tab"),
    Key(["control", "mod1"], "j", lazy.spawn(f"{HOME}/linux_computer/jupyter\ file/jupyter.sh"), desc="Launch jupyter notebook"),
    Key(["control", "mod1"], "p", lazy.spawn(f"{HOME}/.local/share/JetBrains/Toolbox/apps/pycharm-community/bin/pycharm.sh"), desc="Launch pycharm"),
    Key(["control", "mod1"], "r", lazy.spawn(f"{HOME}/.local/share/JetBrains/Toolbox/apps/rustrover/bin/rustrover.sh"), desc="Launch rustrover"),
    Key(["control", "mod1"], "w", lazy.spawn(f"{HOME}/.local/share/JetBrains/Toolbox/apps/webstorm/bin/webstorm.sh"), desc="Launch webstorm"),
    Key(["control", "mod1"], "n", lazy.spawn(f"flatpak run com.github.flxzt.rnote"), desc="Launch rnote"),

    #Windows
    Key([mod], "d", minimise_all(), desc="Minimise all windows"),
    Key([mod], "m", lazy.window.toggle_minimize(), desc="Minimise all windows"),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Move windows between left/right columns or move up/down in current stack.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Resize windows.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left(), desc="Swap window to the left"),
    Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right(), desc="Swap window to the right"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    Key([mod], "s", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #Key([mod, "control"], "w", lazy.spawn("xtrlock -b"), desc="Lock screen"),
    Key([mod, "control"], "w", lazy.spawn("dm-tool lock"), desc="Lock screen"),
    #Key([mod], "Return", lazy.spawncmd(command="bash -ic '%s'"), desc="Spawn a command with aliases in bashrc enabled."),

    #scratchpad
    Key([], "XF86Calculator", lazy.group['scratchpad'].dropdown_toggle('calc'), desc="Bring up calculator scratchpad"),
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
        DropDown("calc", f"{terminal} -- python3 -i {HOME}/linux_computer/jupyter\ file/import.py", height=0.5, y=0, width=0.4, x=0.3, opacity=1),
        DropDown("file", "thunar", height=0.5, y=0.2, width=0.4, x=0.3, opacity=1),
        DropDown("terminal", terminal, height=0.5, y=0.25, width=0.5, x=0.25, opacity=1),
        DropDown("vpn", "protonvpn-app", height=0.5, y=0.22, width=0.08, x=0.39, opacity=1),
        DropDown("volume", "pavucontrol", height=0.5, y=0.2, width=0.4, x=0.3, opacity=1),
        DropDown("bluetooth", "blueman-manager", height=0.5, y=0.2, width=0.4, x=0.3, opacity=1),
        DropDown("wifi", "nm-connection-editor", height=0.5, y=0.2, width=0.4, x=0.3, opacity=1),
    ]),
]

layouts = [
    layout.Columns(
        grow_amount=5,
        wrap_focus_rows=False,
        wrap_focus_columns=False,
        margin=8,
        border_width=0
    ),
    layout.Max(
        margin=8
    ),
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
                widget.Image(
                    filename=f"{HOME}/.config/qtile/widget_icons/open-menu.png",
                    mouse_callbacks = {'Button1': lazy.spawn('xfce4-appfinder')},
                    margin_x=3,
                    margin_y=1
                ),
                widget.TextBox(fmt="  "),
                widget.Image(
                    filename=f"{HOME}/.config/qtile/widget_icons/weather-storm.svg",
                    mouse_callbacks = {'Button1': lazy.spawn(f'{terminal} {HOME}/.config/qtile/mode_switcher.sh')},
                    margin_x=3,
                    margin_y=1
                ),
                widget.TextBox(fmt="  "),
                widget.Image(
                    filename=f"{HOME}/.config/qtile/widget_icons/monitor.svg",
                    mouse_callbacks = {'Button1': lazy.spawn(f'{terminal} {HOME}/.config/qtile/monitor.sh')},
                    margin_x=3,
                    margin_y=1
                ),
                widget.TextBox(fmt="  "),
                widget.CurrentLayoutIcon(
                    margin_x=3,
                    margin_y=1,
                ),
                widget.TextBox(fmt="  "),
                widget.GroupBox(
                    fontsize=22,
                    highlight_method='text',
                    use_mouse_wheel=False,
                    inactive=COLOUR["grey"],
                    margin_x=2,
                    margin_y=2,
                    this_current_screen_border=COLOUR["cyan"]
                ),

                # Middle
                widget.Spacer(),
                widget.Image(
                    filename=f"{HOME}/.config/qtile/widget_icons/office-calendar.svg",
                    margin_y=1
                ),
                widget.Clock(format="  %a %d %b   %H:%M:%S"),
                widget.Spacer(),

                # Right
                widget.Systray(icon_size=22),
                widget.TextBox('   '),

                widget.Image(
                    filename=f"{HOME}/.config/qtile/widget_icons/disk-utility.png",
                    margin_y=1
                ),
                widget.Memory(format=" {MemPercent}%   "),

                widget.Image(
                    filename=f"{HOME}/.config/qtile/widget_icons/network-wireless.png",
                    mouse_callbacks = {'Button1': lazy.group['scratchpad'].dropdown_toggle('wifi')},
                    margin_y=1
                ),
                widget.Net(
                    prefix='M',
                    format=' {down:.2f}{down_suffix}↓↑{up:.2f}{up_suffix}   '
                ),

                widget.Image(
                    filename=f"{HOME}/.config/qtile/widget_icons/utilities-system-monitor.svg",
                    margin_y=1
                ),
                widget.CPU(format=' {load_percent:04.1f}%   '),

                widget.Image(
                    filename=f"{HOME}/.config/qtile/widget_icons/thermal-monitor.svg",
                    margin_y=1
                ),
                widget.ThermalSensor(format=" {temp:.0f}{unit}   "),

                widget.Image(
                    filename=f"{HOME}/.config/qtile/widget_icons/audio-volume-high.svg",
                    mouse_callbacks = {'Button1': lazy.group['scratchpad'].dropdown_toggle('volume')},
                    margin_y=1
                ),
                widget.Volume(fmt=' {}   '),

                widget.BatteryIcon(
                    theme_path=f"{HOME}/.config/qtile/battery_icons",
                    scale=1.1
                ),
                widget.Battery(
                    charge_char='↑',
                    discharge_char='↓',
                    low_percentage=0.2,
                    low_background=COLOUR["red"],
                    low_foreground=COLOUR["white"],
                    format='{char}{percent:2.0%} '
                ),
            ],
            22,
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
bring_front_click = False
floats_kept_above = True
cursor_warp = False

# Float rules
floating_layout = layout.Floating(
    border_width = 0,
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
