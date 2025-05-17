from subprocess import call
from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy

mod = "mod4"
HOME = "/home/minitank"
browser = "firefox-esr"
terminal = "xfce4-terminal --disable-server"

@hook.subscribe.startup_once
def autostart():
    qtile.groups_map["0"].cmd_toscreen()                    # Go to workspace 10 on startup
    call(f"{HOME}/.config/qtile/bash_script/autostart.sh")  # run startup script

keys = [
    # Monitor
    Key([], "XF86Display", lazy.spawn(f'{HOME}/.config/qtile/bash_script/monitor.sh'), desc="Change monitor"),
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
    Key([mod], "s", lazy.spawn(f"{HOME}/.config/qtile/bash_script/spanish.sh"), desc="Practice Spanish"),
    Key([mod], "slash", lazy.spawncmd(command="bash -ic '%s'"), desc="Spawn a command with aliases in bashrc enabled."),
    Key([mod, "shift"], "XF86Touchpadoff", lazy.spawn(f"xfce4-appfinder"), desc="Launch appfinder"),
    Key([mod], "p", lazy.spawn(f"dmenu_run"), desc="Launch appfinder"),
    Key(["control", "mod1"], "f", lazy.spawn(browser), desc="Launch Firefox"),
    Key(["control", "mod1"], "t", lazy.spawn(terminal), desc="Launch terminal"),
    Key(["control", "mod1"], "k", lazy.spawn("kdeconnect-app"), desc="Launch kdeconnect"),
    Key(["control", "mod1"], "o", lazy.spawn("obs"), desc="Launch obs"),
    Key(["control", "mod1"], "g", lazy.spawn("gnome-boxes"), desc="Launch virtual machine"),
    Key(["control", "mod1"], "h", lazy.spawn("thunar"), desc="Launch file explorer"),
    Key(["control", "mod1"], "y", lazy.spawn(f'{browser} --private-window "youtube.com"'), desc="Open youtube on private tab"),
    Key(["control", "mod1"], "j", lazy.spawn(f"{HOME}/linux_computer/jupyter_file/jupyter.sh"), desc="Launch jupyter notebook"),
    Key(["control", "mod1"], "p", lazy.spawn(f"{HOME}/.local/share/JetBrains/Toolbox/apps/pycharm-community/bin/pycharm.sh"), desc="Launch pycharm"),
    Key(["control", "mod1"], "w", lazy.spawn(f"{HOME}/.local/share/JetBrains/Toolbox/apps/webstorm/bin/webstorm.sh"), desc="Launch webstorm"),

    # Switch between windows
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Swap windows
    Key([mod], "m", lazy.layout.swap_main(), desc="Move focus to main"),
    # Resize windows.
    Key([mod], "h", lazy.layout.shrink_main(), desc="Shrink main"),
    Key([mod], "l", lazy.layout.grow_main(), desc="Grow main"),
    Key([mod], "n", lazy.layout.reset(), desc="Reset all window sizes"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod], "i", lazy.next_screen(), desc='Move focus to next monitor'),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"], "w", lazy.spawn("dm-tool lock"), desc="Lock screen"),

    # Scratchpad
    Key([], "XF86Favorites", lazy.group['scratchpad'].dropdown_toggle('calc'), desc="Bring up calculator scratchpad"),
    Key(["control", "mod1"], "c", lazy.group['scratchpad'].dropdown_toggle('calc'), desc="Bring up calculator scratchpad"),
    Key([mod], "semicolon", lazy.group['scratchpad'].dropdown_toggle('file'), desc="Bring up file manager"),
    Key([mod], "Return", lazy.group['scratchpad'].dropdown_toggle('terminal'), desc="Bring up terminal"),
    Key(["control", "mod1"], "v", lazy.group['scratchpad'].dropdown_toggle('vpn'), desc="Bring up vpn"),
]

groups = [Group(i) for i in "1234567890"]

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
            # mod + control + group number = move focused window to group
            Key(
                [mod, "control"], i.name, lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name)
            ),
        ]
    )

# Add scratchpads
groups += [
    ScratchPad("scratchpad", [
        DropDown("calc", f"{terminal} -e 'python3 -i {HOME}/linux_computer/jupyter_file/import.py'", height=0.4, y=0, width=0.4, x=0.3, opacity=1),
        DropDown("file", "thunar", height=0.5, y=0, width=0.7, x=0, opacity=1),
        DropDown("terminal", terminal, height=0.4, y=0, width=0.4, x=0, opacity=1),
        DropDown("vpn", f'{terminal} -e "bash {HOME}/linux_computer/linux_setup/vpn/connect.sh"', height=0.4, y=0, width=0.4, x=0, opacity=1),
    ]),
]

layouts = [
    layout.MonadTall(
        border_normal="#000000",
        border_focus="#00ffff",
        border_width=3,
        new_client_position="top",
        single_border_width=0,
        max_ratio=1,
        min_ratio=0,
    ),
    layout.Max(),
]

widget_defaults = dict(
    font="JetBrainsMono",
    fontsize=22,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    margin_x=5,
                    highlight_method='line',
                    block_highlight_text_color='ffffff',
                    this_current_screen_border='00ffff',
                    highlight_color=['004444', '004444'],
                    active='ffffff',
                    inactive='777777',
                    rounded=False,
                    disable_drag=True,
                    use_mouse_wheel=False,
                ),

                widget.Sep(size_percent=0, linewidth=10),
                widget.CurrentLayoutIcon(scale=0.9),

                # Prompt
                widget.Sep(size_percent=0, linewidth=10),
                widget.Prompt(
                    font="JetBrainsMono",
                    prompt='Run: ',
                    cursor_color='ffffff',
                    bell_style=None,
                ),

                widget.Spacer(),

                # Systray
                widget.Systray(icon_size=24),

                # Weather
                widget.Sep(size_percent=0, linewidth=10),
                widget.TextBox(text=" ", font="Font Awesome", fontsize=20, foreground='00ffff'),
                widget.GenPollCommand(
                    cmd=f"{HOME}/.config/qtile/bash_script/temperature.sh",
                    font="JetBrainsMono",
                    fmt="{}°C",
                    update_interval=3600,
                ),
                widget.Sep(size_percent=0, linewidth=10),
                widget.TextBox(text=" ", font="Font Awesome", fontsize=20, foreground='00ffff'),
                widget.GenPollCommand(
                    cmd=f"{HOME}/.config/qtile/bash_script/humidity.sh",
                    font="JetBrainsMono",
                    fmt="{}%",
                    update_interval=3600,
                ),

                # Net
                widget.Sep(size_percent=0, linewidth=10),
                widget.GenPollCommand(
                    cmd=f"{HOME}/.config/qtile/bash_script/internet.sh",
                    font="Font Awesome",
                    foreground='00ffff',
                    fmt="{} ",
                    fontsize=20,
                    update_interval=2,
                ),
                widget.Net(
                    format='{total:.0f}{total_suffix}',
                    update_interval=2,
                ),

                # Memory
                widget.Sep(size_percent=0, linewidth=10),
                widget.TextBox(text=" ", font="Font Awesome", fontsize=20, foreground='00ffff'),
                widget.Memory(format='{MemPercent}%', update_interval=2),

                # CPU
                widget.Sep(size_percent=0, linewidth=10),
                widget.TextBox(text=" ", font="Font Awesome", fontsize=20, foreground='00ffff'),
                widget.CPU(format='{load_percent}%', update_interval=2),

                # Mode
                widget.Sep(size_percent=0, linewidth=10),
                widget.GenPollCommand(
                    name='mode',
                    cmd=f"{HOME}/.config/qtile/bash_script/mode.sh",
                    font="Font Awesome",
                    foreground='00ffff',
                    fmt="{}",
                    fontsize=20,
                    update_interval=60,
                    mouse_callbacks = {'Button1': lazy.spawn(f'{HOME}/.config/qtile/dunst/mode_switcher.sh')},
                ),

                # Mic
                widget.Sep(size_percent=0, linewidth=10),
                widget.GenPollCommand(
                    name='mic',
                    cmd=f"{HOME}/.config/qtile/bash_script/mic.sh",
                    font="Font Awesome",
                    foreground='00ffff',
                    fmt="{}",
                    fontsize=20,
                    update_interval=60,
                    mouse_callbacks = {'Button1': lazy.spawn(f'{HOME}/.config/qtile/dunst/mic_mute.sh')},
                ),

                # Volume
                widget.Sep(size_percent=0, linewidth=10),
                widget.GenPollCommand(
                    name='mute',
                    cmd=f'{HOME}/.config/qtile/bash_script/mute.sh',
                    font="Font Awesome",
                    foreground='00ffff',
                    fmt="{} ",
                    fontsize=20,
                    update_interval=60,
                    mouse_callbacks = {'Button1': lazy.spawn('pavucontrol')},
                ),
                widget.GenPollCommand(
                    name='volume',
                    cmd=f'{HOME}/.config/qtile/bash_script/volume.sh',
                    font="JetBrainsMono",
                    fmt="{}",
                    update_interval=60,
                    mouse_callbacks = {'Button1': lazy.spawn('pavucontrol')},
                ),

                # Battery
                widget.Sep(size_percent=0, linewidth=10),
                widget.GenPollCommand(
                    cmd=f"{HOME}/.config/qtile/bash_script/battery.sh",
                    font="Font Awesome",
                    foreground='00ffff',
                    fmt="{} ",
                    fontsize=20,
                    update_interval=60,
                ),
                widget.Battery(format='{percent:2.0%}', update_interval=60),

                # Date and time
                widget.Sep(size_percent=0, linewidth=10),
                widget.Clock(format="%a %d %b %H:%M:%S"),
            ],
            26,
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

floating_layout = layout.Floating(
    border_width = 2,
    border_focus = "00ffff",
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='xfce4-appfinder'),
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True

wmname = "Qtile"

