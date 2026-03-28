local wezterm = require("wezterm")
local config = {}

-- Load Pywal colors if available
local pywal_file = os.getenv("HOME") .. "/.cache/wal/wezterm_colors.lua"
if wezterm.fs and wezterm.fs.file_exists(pywal_file) then
    local pywal = dofile(pywal_file)
    config.colors = pywal.colors
else
    config.colors = {
        cursor_bg = "#c0caf5",
        cursor_border = "#c0caf5",
        cursor_fg = "#1a1b26",
        selection_bg = "#33467C",
        selection_fg = "none",
        split = "#7aa2f7",
        scrollbar_thumb = "#545c7e",
    }
end

config.automatically_reload_config = true
config.default_cwd = wezterm.home_dir

-- 🎨 Font Configuration
config.font = wezterm.font_with_fallback({
    { family = "JetBrains Mono",          weight = "Bold" }, -- italic = true --Determination Mono  harfbuzz_features = { "calt=0" }
    { family = "JetBrainsMono Nerd Font", weight = "Bold" }, -- Bold, Medium are the posiible font weight
    { family = "Symbols Nerd Font" },
    { family = "Noto Color Emoji" },
})
config.font_size = 14.5
config.line_height = 1.05
config.cell_width = 1.000

config.color_scheme = "Tokyo Night"

-- 🧱 Tabs / Window / Layout
config.enable_tab_bar = true
config.hide_tab_bar_if_only_one_tab = true -- false --- true
config.window_decorations = "NONE"
config.window_close_confirmation = "NeverPrompt"
config.window_padding = { left = 13, right = 2, top = 13, bottom = 0 }
config.window_frame = {
    font = wezterm.font('JetBrains Mono'),
    font_size = 10.0,
}

config.window_background_opacity = 0.85
config.macos_window_background_blur = nil
config.enable_scroll_bar = true
config.scrollback_lines = 5000

-- 🖼️ Background
config.background = {
    {
        source = { File = wezterm.home_dir .. "/home/waks_work/Pictures/Wallpapers/greenbus.jpg" },
        width = "100%",
        height = "100%",
        opacity = 0.9,
    },
}

-- 🔲 Cursor
config.default_cursor_style = "BlinkingBar"
config.cursor_blink_rate = 600

-- ⌨️ Keybindings
config.keys = {
    { key = "v",        mods = "CTRL|SHIFT", action = wezterm.action.PasteFrom("Clipboard") },
    { key = "c",        mods = "CTRL|SHIFT", action = wezterm.action.CopyTo("Clipboard") },
    { key = "Enter",    mods = "CTRL|SHIFT", action = "ToggleFullScreen" },
    { key = "t",        mods = "CTRL|SHIFT", action = wezterm.action.SpawnTab("CurrentPaneDomain") },
    { key = "w",        mods = "CTRL|SHIFT", action = wezterm.action.CloseCurrentTab({ confirm = true }) },
    { key = "PageUp",   mods = "SHIFT",      action = wezterm.action.ScrollByPage(-1) },
    { key = "PageDown", mods = "SHIFT",      action = wezterm.action.ScrollByPage(1) },
}

config.mouse_bindings = {
    {
        event = { Up = { streak = 1, button = "Left" } },
        mods = "CTRL",
        action = wezterm.action.OpenLinkAtMouseCursor,
    },
}

config.selection_word_boundary = " \t\n{}[]()\"'`"
config.set_environment_variables = { TERM = "xterm-256color" }

-- Title
wezterm.on("format-window-title", function()
    return "WezTerm - Arch Linux"
end)

wezterm.on("format-tab-title", function(tab, tabs, panes, cfg, hover, max_width)
    local title = wezterm.truncate_right(tab.active_pane.title, max_width - 2)
    if tab.is_active then
        return {
            { Attribute = { Intensity = "Bold" } },
            { Text = " " .. title .. " " },
        }
    end
    return { { Text = " " .. title .. " " } }
end)

return config
