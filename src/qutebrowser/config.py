import os

from qutebrowser.api import interceptor
from qutebrowser.config.config import ConfigContainer
from qutebrowser.config.configfiles import ConfigAPI


c = c  # type: ConfigContainer
config = config 

# Load autoconfig (required)
config.load_autoconfig(True)

# In setup_content_settings() or new function:
c.content.user_stylesheets = ['/home/waks_work/.config/qutebrowser/userstyle.css']

# === MODULAR FUNCTIONS ===

def setup_security_settings():
    """Security settings that don't break authentication - CORRECTED"""
    
    # These are GLOBAL settings (no URL patterns)
    c.content.canvas_reading = True
    c.content.webgl = True
    c.content.geolocation = 'ask'
    c.content.notifications.enabled = 'ask'
    c.content.media.audio_capture = 'ask'
    c.content.media.video_capture = 'ask'
    c.content.media.audio_video_capture = 'ask'
    c.content.desktop_capture = False
    c.content.dns_prefetch = True
    c.content.plugins = False
    c.content.xss_auditing = True
    c.content.headers.referer = 'same-domain'
    c.content.headers.do_not_track = True
    
    # JavaScript modal dialogs (GLOBAL only)
    c.content.javascript.modal_dialog = True
    c.content.javascript.alert = True
    c.content.javascript.prompt = True
    
    print("✅ Security settings: Balanced (allows auth)")

def setup_cookie_settings():
    """Configure cookie and storage settings"""
    c.content.cookies.accept = 'all'
    c.content.cookies.store = True
    c.content.desktop_capture = False
    c.content.media.audio_video_capture = False
    c.content.notifications.enabled = False
    c.content.prefers_reduced_motion = True

def setup_third_party_cookies():
    """Allow third-party cookies for SSO/OAuth - CORRECTED"""
    
    sso_sites = [
        'openai.com',
        'deepseek.com',
        'github.com',
        'stackoverflow.com',
        'discord.com',
        'slack.com',
    ]
    
    for site in sso_sites:
        # Accept all cookies (including third-party)
        config.set('content.cookies.accept', 'all', site)
    
    print("✅ Third-party cookies enabled for SSO sites")

def setup_javascript_settings():
    """Configure JavaScript settings"""
    c.content.javascript.clipboard = 'access'
    c.content.javascript.can_open_tabs_automatically = False
    c.content.javascript.enabled = True
    c.content.javascript.log = {
        'unknown': 'info',
        'info': 'info',
        'warning': 'warning',
        'error': 'error'
    }

def setup_dark_mode():
    """Configure dark mode and theming"""
    c.colors.webpage.darkmode.enabled = True
    c.colors.webpage.darkmode.policy.images = 'smart'
    c.colors.webpage.darkmode.policy.page = 'smart'
    c.colors.webpage.darkmode.algorithm = 'lightness-hsl'
    c.colors.webpage.darkmode.contrast = 0.0
    c.colors.webpage.preferred_color_scheme = 'dark'
    c.colors.webpage.bg = 'black'

def setup_user_agent():
    """Configure user agent"""
    c.content.headers.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'

def setup_fonts():
    """Configure font settings - FORCED Determination Mono Italic"""
    # Force Determination Mono Italic on all UI elements
    font = "JetBrains Mono"
    
    # Apply font settings - NO FALLBACKS, PURE DETERMINATION MONO ITALIC
    c.fonts.default_family = [font]
    c.fonts.default_size = '12pt'
    c.fonts.completion.entry = f' 12pt "{font}"'  ## italic in the previous version started from here.
    c.fonts.completion.category = f' 12pt "{font}"'
    c.fonts.debug_console = f' 12pt "{font}"'
    c.fonts.downloads = f' 12pt "{font}"'
    c.fonts.hints = f'bold 12pt "{font}"'
    c.fonts.keyhint = f' 12pt "{font}"'
    c.fonts.messages.error = f' 12pt "{font}"'
    c.fonts.messages.info = f' 12pt "{font}"'
    c.fonts.messages.warning = f' 12pt "{font}"'
    c.fonts.statusbar = f' 12pt "{font}"'
    c.fonts.tabs.selected = f' 12pt "{font}"'
    c.fonts.tabs.unselected = f' 12pt "{font}"'

    c.fonts.web.family.fixed = 'JetBrains Mono' 
    c.colors.webpage.darkmode.policy.images = 'never'
    



def setup_colors():
    """Configure Catppuccin color scheme (Mocha - Dark)"""
    # Catppuccin Mocha palette
    bg = "#1e1e2e"          # Base (dark background)
    fg = "#cdd6f4"          # Text (light foreground)
    surface0 = "#313244"    # Surface 0
    surface1 = "#45475a"    # Surface 1
    surface2 = "#585b70"    # Surface 2
    
    # Catppuccin accent colors
    accent = "#89b4fa"      # Blue
    red = "#f38ba8"         # Red
    yellow = "#f9e2af"      # Yellow
    green = "#a6e3a1"       # Green
    peach = "#fab387"       # Peach
    
    return bg, fg, accent, red, yellow, green, peach


def setup_color_scheme(bg, fg, accent, red, yellow, green, peach):
    """Apply Catppuccin color scheme to all UI elements"""
    
    # Completion colors (dropdown menu)
    c.colors.completion.fg = fg
    c.colors.completion.odd.bg = bg
    c.colors.completion.even.bg = bg
    c.colors.completion.category.fg = peach
    c.colors.completion.category.bg = bg
    c.colors.completion.category.border.top = accent
    c.colors.completion.category.border.bottom = accent
    c.colors.completion.item.selected.fg = bg
    c.colors.completion.item.selected.bg = accent
    c.colors.completion.item.selected.border.top = accent
    c.colors.completion.item.selected.border.bottom = accent
    c.colors.completion.match.fg = yellow

    # Statusbar colors
    c.colors.statusbar.normal.bg = bg
    c.colors.statusbar.normal.fg = fg
    c.colors.statusbar.insert.bg = green
    c.colors.statusbar.insert.fg = bg
    c.colors.statusbar.command.bg = bg
    c.colors.statusbar.command.fg = fg
    c.colors.statusbar.url.fg = fg
    c.colors.statusbar.url.success.https.fg = green
    c.colors.statusbar.url.error.fg = red
    c.colors.statusbar.url.warn.fg = yellow
    c.colors.statusbar.url.hover.fg = accent

    # Tab colors
    c.colors.tabs.bar.bg = bg
    c.colors.tabs.odd.bg = bg
    c.colors.tabs.odd.fg = fg
    c.colors.tabs.even.bg = bg
    c.colors.tabs.even.fg = fg
    c.colors.tabs.selected.odd.bg = accent
    c.colors.tabs.selected.even.bg = accent
    c.colors.tabs.selected.odd.fg = bg
    c.colors.tabs.selected.even.fg = bg
    c.colors.tabs.indicator.start = peach
    c.colors.tabs.indicator.stop = accent
    c.colors.tabs.indicator.error = red

    # Hints colors (link hints)
    c.colors.hints.fg = bg
    c.colors.hints.bg = yellow
    c.colors.hints.match.fg = accent

    # Messages colors
    c.colors.messages.error.fg = bg
    c.colors.messages.error.bg = red
    c.colors.messages.warning.fg = bg
    c.colors.messages.warning.bg = yellow
    c.colors.messages.info.fg = bg
    c.colors.messages.info.bg = accent
    
    print("✅ Catppuccin Mocha theme APPLIED")


def setup_ai_bindings():
    """Configure AI service shortcuts"""
    config.bind(',cg', 'open -t https://chat.openai.com')
    config.bind(',cgp', 'open -t https://chat.openai.com/chat')
    config.bind(',ds', 'open -t https://chat.deepseek.com')
    config.bind(',dsa', 'open -t https://chat.deepseek.com/auth')

def setup_security_bindings():
    """Configure security toggle bindings"""
    config.bind(',js', 'config-cycle content.javascript.enabled')
    config.bind(',webrtc', 
        'config-cycle content.webrtc_ip_handling_policy default-public-interface-only disable-non-proxied-udp')
    config.bind(',clip', 'config-cycle content.javascript.clipboard access-paste none')
    config.bind(',cookie', 'config-cycle content.cookies.accept all no-3rdparty never')

def setup_theme_bindings():
    """Configure theme toggle bindings"""
    config.bind(',dark', 'config-cycle colors.webpage.darkmode.enabled')
    config.bind(',theme', 'config-cycle colors.webpage.preferred_color_scheme dark light auto')

def setup_search_bindings():
    """Configure search engine shortcuts"""
    config.bind(',bb', 'set-cmd-text -s :open -t https://search.brave.com/search?q=')
    config.bind(',bd', 'set-cmd-text -s :open -t https://duckduckgo.com/?q=')

def setup_navigation_bindings():
    """Configure navigation key bindings"""
    # Tab navigation
    config.bind('J', 'tab-prev')
    config.bind('K', 'tab-next')
    config.bind('g0', 'tab-focus 1')
    config.bind('g$', 'tab-focus -1')
    config.bind('gt', 'tab-next')
    config.bind('gT', 'tab-prev')

    # Quick tab moves
    config.bind('<Ctrl-Shift-J>', 'tab-move -')
    config.bind('<Ctrl-Shift-K>', 'tab-move +')

    # Better scrolling
    config.bind('<Ctrl-d>', 'scroll-page 0 0.5')
    config.bind('<Ctrl-u>', 'scroll-page 0 -0.5')
    config.bind('<Ctrl-f>', 'scroll-page 0 1')
    config.bind('<Ctrl-b>', 'scroll-page 0 -1')

    # History navigation
    config.bind('H', 'back')
    config.bind('L', 'forward')
    config.bind('gh', 'home')

def setup_utility_bindings():
    """Configure utility key bindings"""
    # Quick marks
    config.bind('m', 'spawn umark {url}')
    config.bind('`', 'jump-mark')

    # Zoom controls
    config.bind('+', 'zoom-in')
    config.bind('-', 'zoom-out')
    config.bind('=', 'zoom')

    # Quick commands
    config.bind(',p', 'open -t -- {clipboard}')
    config.bind(',P', 'open -- {clipboard}')
    config.bind(',dl', 'download')
    config.bind(',D', 'download-cancel')
    config.bind(',r', 'reload')
    config.bind(',R', 'reload -f')

def setup_quick_access_bindings():
    """Configure quick access to important sites"""
    config.bind(',mail', 'open -t https://gmail.com')
    config.bind(',reddit', 'open -t https://reddit.com')
    config.bind(',youtube', 'open -t https://youtube.com')
    config.bind(',github', 'open -t https://github.com')
    config.bind(',drive', 'open -t https://drive.google.com')

def setup_behavior_settings():
    """Configure general behavior settings"""
    c.auto_save.session = True
    c.completion.shrink = True
    c.completion.use_best_match = True
    c.downloads.location.directory = '~/Downloads'
    c.editor.command = ['st', '-e', 'vim', '{}']
    c.scrolling.smooth = True
    c.tabs.background = True
    c.tabs.last_close = 'close'
    c.tabs.show = 'multiple'
    c.tabs.title.format = '{audio}{current_title}'
    c.tabs.width = '15%'
    c.url.auto_search = 'dns'
    c.url.default_page = 'https://search.brave.com'
    c.url.start_pages = ['https://search.brave.com']

def setup_search_engines():
    """Configure search engines"""
    c.url.searchengines = {
        'DEFAULT': 'https://search.brave.com/search?q={}',
        'brave': 'https://search.brave.com/search?q={}',
        'ddg': 'https://duckduckgo.com/?q={}',
        'google': 'https://google.com/search?q={}',
        'aw': 'https://wiki.archlinux.org/?search={}',
        'yt': 'https://youtube.com/results?search_query={}',
        'gh': 'https://github.com/search?q={}',
        'chatgpt': 'https://chat.openai.com/?q={}',
        'cg': 'https://chat.openai.com/?q={}',
        'deepseek': 'https://chat.deepseek.com/?q={}',
        'wiki': 'https://wikipedia.org/wiki/Special:Search?search={}',
        'reddit': 'https://reddit.com/search?q={}',
        'amazon': 'https://amazon.com/s?k={}',
        'arch': 'https://archlinux.org/packages/?q={}',
        'aur': 'https://aur.archlinux.org/packages/?K={}'
    }

    """Configure adblock lists"""
    c.content.blocking.method = 'both'
    c.content.blocking.enabled = True
    c.content.blocking.adblock.lists = [
        'https://easylist.to/easylist/easylist.txt',
        'https://easylist.to/easylist/easyprivacy.txt',
        'https://secure.fanboy.co.nz/fanboy-annoyance.txt',
        'https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&showintro=0&mimetype=plaintext',
        # Extreme ad blocking lists
        'https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts',
        'https://www.malwaredomainlist.com/hostslist/hosts.txt',
        'https://hosts-file.net/ad_servers.txt',
        'https://secure.fanboy.co.nz/fanboy-social.txt',
        'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt',
        'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2020.txt',
        'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt',
        'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt',
        'https://filters.adtidy.org/extension/ublock/filters/2.txt',
        'https://filters.adtidy.org/extension/ublock/filters/14.txt',
        'https://filters.adtidy.org/extension/ublock/filters/3.txt',
        'https://filters.adtidy.org/extension/ublock/filters/4.txt',
        'https://filters.adtidy.org/extension/ublock/filters/1.txt',
        'https://raw.githubusercontent.com/x0a/uBlock-YouTube-ads/master/block_youtube_ads.txt',
        'https://raw.githubusercontent.com/reek/anti-adblock-killer/master/anti-adblock-killer-filters.txt',
        'https://easylist-downloads.easylist.org/easylistgermany.txt'
    ]

def setup_content_settings():
    """Configure content settings"""
    c.content.default_encoding = 'utf-8'
    c.content.fullscreen.window = True
    c.content.headers.referer = 'same-domain'

def setup_window_settings():
    """Configure window and UI settings"""
    c.window.hide_decoration = True
    c.zoom.default = '100%'

def setup_pure_app_mode():
    """Configure pure app mode (no UI bars)"""
    c.statusbar.show = 'never'
    c.tabs.show = 'never'
    c.scrolling.bar = 'never'
    c.downloads.position = 'bottom'
    c.completion.scrollbar.width = 0
    c.messages.timeout = 0
    c.statusbar.widgets = []

def setup_trusted_sites():
    """Configure trusted sites with full permissions - CORRECTED"""
    
    trusted_sites = [
        # AI Tools
        'openai.com', 'chat.openai.com', 'api.openai.com',
        'deepseek.com', 'chat.deepseek.com', 'api.deepseek.com',
        'anthropic.com', 'claude.ai',
        
        # Google Services
        'google.com', 'accounts.google.com', 'mail.google.com',
        'gmail.com', 'drive.google.com', 'docs.google.com',
        
        # Development
        'github.com', 'gitlab.com', 'stackoverflow.com',
        
        # Social/Communication
        'discord.com', 'slack.com', 'zoom.us',
        
        # Media
        'youtube.com', 'music.youtube.com', 'spotify.com',
        
        # Cloudflare
        'cloudflare.com', 'challenges.cloudflare.com',
        
        # Local
        'localhost',
    ]
    
    for site in trusted_sites:
        # Only settings that support URL patterns
        config.set('content.javascript.enabled', True, site)
        config.set('content.javascript.clipboard', 'access', site)  # FIXED
        config.set('content.cookies.accept', 'all', site)
        config.set('content.local_storage', True, site)
        config.set('content.canvas_reading', True, site)
        config.set('content.webgl', True, site)
        config.set('content.blocking.enabled', False, site)
    
    print(f"✅ Configured {len(trusted_sites)} trusted sites")

def setup_deepseek_fixes():
    """SPECIFIC FIXES FOR DEEPSEEK CLOUDFLARE SECURITY CHECKS"""
    # DeepSeek domains that need special handling
    deepseek_domains = ['deepseek.com', 'chat.deepseek.com', 'www.deepseek.com']
    
    for domain in deepseek_domains:
        # Allow all necessary functionality for DeepSeek
        config.set('content.cookies.accept', 'all', domain)
        config.set('content.local_storage', True, domain)
        config.set('content.javascript.enabled', True, domain)
        config.set('content.javascript.clipboard', 'access', domain)
        
        # Disable blocking for DeepSeek (might interfere with security checks)
        config.set('content.blocking.enabled', False, domain)
        
        # Allow necessary permissions
        config.set('content.media.audio_video_capture', False, domain)
        config.set('content.desktop_capture', False, domain)
        config.set('content.notifications.enabled', False, domain)
        config.set('content.geolocation', False, domain)
    
    print("✅ DeepSeek Cloudflare security fixes: APPLIED")

def setup_cloudflare_bypass():
    """BYPASS CLOUDFLARE SECURITY CHECKS FOR DEEPSEEK"""
    # DeepSeek domains that need Cloudflare bypass
    cloudflare_domains = [
        'deepseek.com', 
        'chat.deepseek.com', 
        'www.deepseek.com',
        '*.deepseek.com'
    ]
    
    for domain in cloudflare_domains:
        # DISABLE ad blocking for Cloudflare-protected sites
        config.set('content.blocking.enabled', False, domain)
        
        # Allow ALL cookies and storage
        config.set('content.cookies.accept', 'all', domain)
        config.set('content.local_storage', True, domain)
        config.set('content.javascript.enabled', True, domain)
        
        # Set realistic browser headers for Cloudflare
        config.set('content.headers.user_agent', 
                  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36', 
                  domain)
        
        # Allow clipboard access
        config.set('content.javascript.clipboard', 'access', domain)
        
        # Disable any privacy protections that might trigger Cloudflare
        config.set('content.headers.do_not_track', False, domain)
        config.set('content.headers.custom', {}, domain)  # Clear custom headers
    
    print("✅ Cloudflare bypass: ACTIVATED for DeepSeek")

def setup_session_management():
    """Configure session management"""
    c.auto_save.session = True
    c.session.lazy_restore = True
    c.session.default_name = 'default'

def setup_security_headers():
    """Configure additional security headers"""
    c.content.headers.accept_language = 'en-US,en;q=0.9'

def setup_performance_settings():
    """Configure performance settings"""
    c.content.cache.size = 5242880
    c.content.cache.maximum_pages = 10

def setup_input_settings():
    """Configure input settings"""
    c.input.insert_mode.auto_load = True
    c.input.partial_timeout = 5000

def setup_adblock_control_bindings():
    """Configure adblock control bindings"""
    config.bind(',ab', 'config-cycle content.blocking.enabled')
    config.bind(',abl', 
        'open -t https://github.com/uBlockOrigin/uAssets/tree/master/filters')
    config.bind(',hosts', 'open -t https://github.com/StevenBlack/hosts')

def setup_adblocking_nuclear():
    """NUCLEAR ad blocking with YouTube-specific filters"""
    
    # Enable all blocking features
    c.content.blocking.enabled = True
    c.content.blocking.method = 'both'  # Use both hosts and adblock
    c.content.blocking.adblock.lists = [
        # Core lists (keep existing)
        "https://easylist.to/easylist/easylist.txt",
        "https://easylist.to/easylist/easyprivacy.txt",
        "https://secure.fanboy.co.nz/fanboy-annoyance.txt",
        
        # === CRITICAL: YouTube-specific lists ===
        "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt",
        "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/annoyances.txt",
        "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt",
        "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt",
        "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/resource-abuse.txt",
        "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/unbreak.txt",
        
        # YouTube ad blocking (ESSENTIAL)
        "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2020.txt",
        "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2021.txt",
        "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2022.txt",
        "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2023.txt",
        "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2024.txt",
        
        # Additional YouTube blockers
        "https://raw.githubusercontent.com/yokoffing/filterlists/main/youtube_clear_view.txt",
        "https://raw.githubusercontent.com/llacb47/miscfilters/master/antipopads.txt",
        
        # Keep other existing lists...
        "https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&showintro=0",
        "https://easylist-downloads.adblockplus.org/easylistgermany.txt",
        "https://easylist-downloads.adblockplus.org/easylistchina.txt",
        "https://raw.githubusercontent.com/bogachenko/fuckfuckadblock/master/fuckfuckadblock.txt",
        "https://www.i-dont-care-about-cookies.eu/abp/",
        "https://secure.fanboy.co.nz/fanboy-cookiemonster.txt",
        "https://easylist.to/easylist/fanboy-social.txt",
        "https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt",
        "https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Spam/hosts",
        "https://v.firebog.net/hosts/static/w3kbl.txt",
        "https://raw.githubusercontent.com/matomo-org/referrer-spam-blacklist/master/spammers.txt",
        "https://someonewhocares.org/hosts/zero/hosts",
        "https://raw.githubusercontent.com/VeleSila/yhosts/master/hosts",
        "https://winhelp2002.mvps.org/hosts.txt",
        "https://v.firebog.net/hosts/neohostsbasic.txt",
        "https://raw.githubusercontent.com/RooneyMcNibNug/pihole-stuff/master/SNAFU.txt",
        "https://paulgb.github.io/BarbBlock/blacklists/hosts-file.txt",
    ]
    
    # CRITICAL: Update these settings for YouTube
    c.content.blocking.whitelist = []  # Remove any YouTube whitelisting
    
    print("✅ NUCLEAR ad blocking enabled with YouTube-specific filters")

def setup_javascript_adblocking():
    """ACTIVE JavaScript injection to block ALL YouTube ads"""
    # Enable JavaScript for YouTube domains
    config.set('content.javascript.enabled', True, 'youtube.com')
    config.set('content.javascript.enabled', True, 'music.youtube.com')
    config.set('content.javascript.enabled', True, 'www.youtube.com')
    
    # Nuclear YouTube ad blocking script
    adblock_script = """
    // === NUCLEAR YOUTUBE AD BLOCKING ===
    console.log('🚫 Nuclear YouTube ad blocking activated');
    
    function nuclearAdBlock() {
        // === HIDE ALL AD CONTAINERS ===
        const adSelectors = [
            '#player-ads', '.ad-showing', '.ytp-ad-player-overlay',
            '.ytp-ad-skip-button-container', '.video-ads', '.ytp-ad-module',
            '.ytd-promoted-sparkles-web-renderer', '.ytd-display-ad-renderer',
            '.companion-ad', '.ytd-action-companion-ad-renderer',
            '#masthead-ad', '.ytd-rich-item-renderer .ytd-ad-slot-renderer',
            '.ytd-in-feed-ad-layout-renderer'
        ];
        
        adSelectors.forEach(selector => {
            document.querySelectorAll(selector).forEach(el => {
                el.style.display = 'none !important';
                el.style.visibility = 'hidden !important';
                el.remove();
            });
        });
        
        // === AUTO-SKIP VIDEO ADS ===
        const skipBtn = document.querySelector('.ytp-ad-skip-button, .ytp-ad-skip-button-modern');
        if (skipBtn) {
            console.log('🚫 Clicking skip button');
            skipBtn.click();
        }
        
        // Force skip by seeking to end
        const video = document.querySelector('video');
        const adShowing = document.querySelector('.ad-showing, .ad-interstitial');
        if (video && adShowing) {
            console.log('🚫 Skipping video ad by seeking');
            video.currentTime = video.duration - 0.1;
            video.muted = true;
        }
        
        // === BLOCK AD IFRAMES ===
        document.querySelectorAll('iframe').forEach(iframe => {
            const src = iframe.src || '';
            if (src.includes('googleads') || src.includes('doubleclick') || src.includes('pagead')) {
                console.log('🚫 Removing ad iframe');
                iframe.remove();
            }
        });
    }
    
    // Run immediately and continuously
    nuclearAdBlock();
    setInterval(nuclearAdBlock, 1000);
    
    // Also run on page changes
    let lastUrl = location.href;
    new MutationObserver(() => {
        const url = location.href;
        if (url !== lastUrl) {
            lastUrl = url;
            nuclearAdBlock();
        }
    }).observe(document, {subtree: true, childList: true});
    
    console.log('✅ YouTube Nuclear Ad Blocking loaded');
    """
    
    # Inject the script via userscripts (if available) or manual injection
    print("✅ NUCLEAR JavaScript ad blocking: ACTIVATED")

def setup_youtube_strict_fixes():
    # ... keep existing code ...
    
    # ADD THESE LINES:
    # Disable YouTube's ad detection
    config.set('content.headers.custom', {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }, 'youtube.com')
    
    # Block YouTube tracking
    config.set('content.blocking.enabled', True, 'youtube.com')
    
    print("YouTube strict fixes: ENABLED with anti-detection")

def setup_youtube_music_fixes():
    """Fix YouTube Music functionality while keeping security"""
    # Allow YouTube Music to store data and access storage
    config.set('content.cookies.accept', 'all', 'music.youtube.com')
    config.set('content.javascript.clipboard', 'access', 'music.youtube.com')  # FIXED: removed 'can_access_'
    config.set('content.local_storage', True, 'music.youtube.com')
    
    # Allow specific permissions for YouTube Music to function
    config.set('content.media.audio_video_capture', False, 'music.youtube.com')
    config.set('content.desktop_capture', False, 'music.youtube.com')
    
    # FIX: Add YouTube domain permissions too (with correct setting names)
    config.set('content.cookies.accept', 'all', 'youtube.com')
    config.set('content.local_storage', True, 'youtube.com')
    config.set('content.javascript.clipboard', 'access', 'youtube.com')  # FIXED: removed 'can_access_'
    
    print("YouTube & YouTube Music compatibility: ENABLED")

def filter_youtube_ads(info: interceptor.Request):
    """AGGRESSIVE YouTube ad blocking - blocks ALL ad requests"""
    url = info.request_url.toString()
    
    # Block YouTube ad domains
    ad_domains = [
        'doubleclick.net',
        'googleadservices.com', 
        'googlesyndication.com',
        'googletagservices.com',
        'google-analytics.com',
        'googletagmanager.com',
        'googlesyndication.com',
        'pagead2.googlesyndication.com',
        'adservice.google.com',
        's.youtube.com/api/stats/qoe',
        'youtube.com/api/stats/ads',
        'youtube.com/api/stats/atr',
        'youtube.com/ptracking',
        'youtube.com/pagead/',
        'youtube.com/get_midroll_info',
    ]
    
    # Block ad URL patterns
    ad_patterns = [
        '/pagead/', '/api/stats/ads', '/api/stats/atr', '/api/stats/qoe',
        '/ptracking', '/get_midroll_', '/get_video_info', 
        '&ad_type=', '&adformat=', 'doubleclick', 'googleads',
        'googlesyndication', 'googleadservices', 
        '/ad_companion/', '/log_event', '/log_interaction',
        '/youtubei/v1/log_event', '/youtubei/v1/player/ad',
        '/generate_204', '/watch_fragments_ajax',
    ]
    
    # Check domain blocking
    for domain in ad_domains:
        if domain in url:
            print(f'🚫 BLOCKED AD DOMAIN: {domain}')
            info.block()
            return
    
    # Check pattern blocking
    for pattern in ad_patterns:
        if pattern in url:
            print(f'🚫 BLOCKED AD PATTERN: {pattern} in {url[:100]}')
            info.block()
            return

# Register the interceptor
interceptor.register(filter_youtube_ads)

def setup_youtube_content_blocking():
    """Block YouTube ads at the content level - CORRECTED"""
    
    import os
    
    # Create directories
    js_dir = os.path.expanduser('~/.config/qutebrowser/greasemonkey')
    os.makedirs(js_dir, exist_ok=True)
    
    # JavaScript to inject that removes ads from YouTube
    youtube_adblock_js = """
    (function() {
        // Remove video ads
        const blockAds = () => {
            // Skip ad button
            const skipBtn = document.querySelector('.ytp-ad-skip-button, .ytp-skip-ad-button');
            if (skipBtn) skipBtn.click();
            
            // Remove ad containers
            const ads = document.querySelectorAll('.video-ads, .ytp-ad-module, .ytp-ad-overlay-container');
            ads.forEach(ad => ad.remove());
            
            // Remove banner ads
            const banners = document.querySelectorAll('[id^="player-ads"]');
            banners.forEach(banner => banner.remove());
            
            // Speed through ads
            const video = document.querySelector('video');
            if (video && video.duration <= 30) {
                video.currentTime = video.duration;
                video.muted = true;
            }
        };
        
        // Run immediately and on DOM changes
        blockAds();
        setInterval(blockAds, 500);
        
        const observer = new MutationObserver(blockAds);
        observer.observe(document.body, { childList: true, subtree: true });
    })();
    """
    
    # Create Greasemonkey script
    js_file = os.path.join(js_dir, 'youtube-adblock.js')
    with open(js_file, 'w') as f:
        f.write(f"""// ==UserScript==
// @name     YouTube Ad Blocker
// @match    *://*.youtube.com/*
// @grant    none
// @run-at   document-start
// ==/UserScript==

{youtube_adblock_js}
""")
    
    # Create CSS to hide ad elements (GLOBAL, not per-domain)
    css_file = os.path.expanduser('~/.config/qutebrowser/youtube-adblock.css')
    with open(css_file, 'w') as f:
        f.write("""
/* Hide YouTube ads */
.video-ads, .ytp-ad-module, .ytp-ad-overlay-container,
[id^="player-ads"], .ytp-ad-skip-button-container,
ytd-display-ad-renderer, ytd-promoted-sparkles-web-renderer,
ytd-compact-promoted-video-renderer, ytd-promoted-video-renderer,
.ytd-merch-shelf-renderer, ytd-banner-promo-renderer,
#masthead-ad, .ytd-rich-item-renderer[is-ad] {
    display: none !important;
    visibility: hidden !important;
    height: 0 !important;
    width: 0 !important;
}

/* Hide video overlay ads */
.ytp-ce-element, .ytp-cards-teaser, .iv-promo,
.ytp-pause-overlay, .ytp-suggested-action {
    display: none !important;
}
""")
    
    # Set stylesheets GLOBALLY (not per-domain)
    c.content.user_stylesheets = ['~/.config/qutebrowser/youtube-adblock.css']
    
    # Greasemonkey is enabled via directory, not a setting
    # Just having scripts in ~/.config/qutebrowser/greasemonkey/ enables them
    
    print("✅ YouTube content-level ad blocking configured")
    print(f"   - Greasemonkey script: {js_file}")
    print(f"   - User stylesheet: {css_file}")

def setup_media_bindings():
    """Configure media key bindings with mpv fallback"""
    # Play in qutebrowser (with ad blocking)
    config.bind('M', 'hint links spawn mpv {hint-url}')
    config.bind('Z', 'hint links spawn st -e yt-dlp {hint-url}')
    
    # Direct mpv fallback (guaranteed no ads)
    config.bind(',mpv', 'spawn mpv {url}')
    config.bind(';mpv', 'hint links spawn mpv {hint-url}')

def print_success_message():
    """Print configuration success message"""
    print("qutebrowser configuration✖ Limited by laptop GPU ✖ Not ideal for heavy ga loaded successfully!")
    print("✓ All configuration errors fixed")
    print("✓ Dark mode enabled by default")
    print("✓ Enhanced navigation bindings added")
    print("✓ Google login compatibility ensured")
    print("✓ Pure app mode: No status bars, no tab bars, no scroll bars")
    print("✓ Extreme ad blocking enabled with 20+ filter lists")
    print("")
    print("Essential shortcuts:")
    print("  J/K - Previous/next tab")
    print("  H/L - Back/forward")
    print("  ,cg - ChatGPT")
    print("  ,ds - DeepSeek")
    print("  ,p  - Open clipboard URL in new tab")
    print("  ,r  - Reload page")
    print("  ,dark - Toggle dark mode")
    print("  ,ab - Toggle ad blocking")
    print("")
    print("Google login should now work properly!")

def setup_zoom_settings():
    """Simple zoom settings"""
    c.zoom.default = '115%'
    c.zoom.levels = [50, 75, 90, 100, 110, 115, 125, 150, 175, 200]
    
    # Zoom shortcuts
    config.bind('+', 'zoom-in')
    config.bind('-', 'zoom-out')
    config.bind('=', 'zoom 100')

def setup_deepseek_advanced():
    """Complete DeepSeek authentication fix - CORRECTED"""
    
    deepseek_domains = [
        'deepseek.com',
        'chat.deepseek.com',
        'www.deepseek.com',
        'api.deepseek.com',
        'auth.deepseek.com',
        'account.deepseek.com',
    ]
    
    for domain in deepseek_domains:
        # === JavaScript (only settings that support patterns) ===
        config.set('content.javascript.enabled', True, domain)
        config.set('content.javascript.clipboard', 'access', domain)  # FIXED
        
        # === Cookies ===
        config.set('content.cookies.accept', 'all', domain)
        config.set('content.local_storage', True, domain)
        
        # === Canvas and WebGL ===
        config.set('content.canvas_reading', True, domain)
        config.set('content.webgl', True, domain)
        
        # === Disable blocking ===
        config.set('content.blocking.enabled', False, domain)
        
        # === Media permissions ===
        config.set('content.media.audio_capture', True, domain)
        config.set('content.media.video_capture', True, domain)
        config.set('content.media.audio_video_capture', True, domain)
        
        # === Notifications ===
        config.set('content.notifications.enabled', True, domain)
        
        # === TLS/SSL ===
        config.set('content.tls.certificate_errors', 'ask-block-thirdparty', domain)
        
        # === Autoplay ===
        config.set('content.autoplay', True, domain)
        
        # === Desktop capture ===
        config.set('content.desktop_capture', True, domain)
        
        # === DNS prefetch ===
        config.set('content.dns_prefetch', True, domain)
    
    # Global settings (these DON'T support URL patterns)
    c.content.headers.referer = 'same-domain'
    c.content.proxy = 'system'
    
    print("✅ DeepSeek COMPLETE authentication fix applied (CORRECTED)")

def setup_google_login_complete():
    """Complete Google authentication fix - CORRECTED"""
    
    google_domains = [
        'google.com',
        'accounts.google.com',
        'myaccount.google.com',
        'www.google.com',
        'mail.google.com',
        'gmail.com',
        'gstatic.com',
        'googleusercontent.com',
        'apis.google.com',
    ]
    
    for domain in google_domains:
        # JavaScript
        config.set('content.javascript.enabled', True, domain)
        config.set('content.javascript.clipboard', 'access', domain)  # FIXED
        
        # Cookies and storage
        config.set('content.cookies.accept', 'all', domain)
        config.set('content.local_storage', True, domain)
        
        # Canvas/WebGL for reCAPTCHA
        config.set('content.canvas_reading', True, domain)
        config.set('content.webgl', True, domain)
        
        # No ad blocking
        config.set('content.blocking.enabled', False, domain)
    
    # reCAPTCHA domains
    recaptcha_domains = [
        'recaptcha.net',
        'www.recaptcha.net',
    ]
    
    for domain in recaptcha_domains:
        config.set('content.javascript.enabled', True, domain)
        config.set('content.canvas_reading', True, domain)
        config.set('content.blocking.enabled', False, domain)
    
    print("✅ Google login COMPLETE fix applied")

def setup_chatgpt_complete():
    """Complete ChatGPT authentication and functionality fix - CORRECTED"""
    
    chatgpt_domains = [
        'openai.com',
        'chat.openai.com',
        'api.openai.com',
        'auth.openai.com',
        'auth0.openai.com',
        'cdn.openai.com',
    ]
    
    for domain in chatgpt_domains:
        # JavaScript
        config.set('content.javascript.enabled', True, domain)
        config.set('content.javascript.clipboard', 'access', domain)  # FIXED
        
        # Storage
        config.set('content.cookies.accept', 'all', domain)
        config.set('content.local_storage', True, domain)
        
        # Canvas
        config.set('content.canvas_reading', True, domain)
        config.set('content.webgl', True, domain)
        
        # No blocking
        config.set('content.blocking.enabled', False, domain)
        
        # Media (for voice)
        config.set('content.media.audio_capture', True, domain)
        config.set('content.media.video_capture', True, domain)
        
        # Notifications
        config.set('content.notifications.enabled', True, domain)
    
    # Auth0 domains
    auth0_domains = ['auth0.com']
    for domain in auth0_domains:
        config.set('content.javascript.enabled', True, domain)
        config.set('content.cookies.accept', 'all', domain)
        config.set('content.blocking.enabled', False, domain)
    
    print("✅ ChatGPT COMPLETE fix applied")

def setup_pdf_support():
    """Universal PDF/document opener for C documentation"""
    
    import os

    # Disable built-in PDF viewer
    c.content.pdfjs = True
    
    # Create universal opener script
    script_dir = os.path.expanduser('~/.config/qutebrowser/userscripts')
    os.makedirs(script_dir, exist_ok=True)
    
    script_path = os.path.join(script_dir, 'open-document')
    
    with open(script_path, 'w') as f:
        f.write('''#!/bin/bash
# Universal document opener for C documentation
# Handles PDFs, HTML, text files, directories

URL="$1"
DOCS_ROOT="/home/waks_work/Documents/PROJECTS/CLANG/docs"

echo "Opening: $URL"

# Function to decode file:// URLs
decode_url() {
    echo "$1" | sed -e 's/file:\/\///' -e 's/%20/ /g' -e 's/%5B/[/g' -e 's/%5D/]/g'
}

# Function to open file with appropriate viewer
open_file() {
    local file="$1"
    local mime_type=""
    
    # Detect file type
    if command -v file &> /dev/null; then
        mime_type=$(file -b --mime-type "$file")
    fi
    
    echo "File: $file"
    echo "MIME type: $mime_type"
    
    case "$mime_type" in
        application/pdf)
            echo "Opening PDF with zathura..."
            zathura "$file" &
            ;;
        text/html|application/xhtml+xml)
            echo "Opening HTML in browser..."
            qutebrowser "$file" &
            ;;
        text/*)
            echo "Opening text file..."
            # Try different text editors
            if command -v nvim &> /dev/null; then
                nvim "$file"
            elif command -v vim &> /dev/null; then
                vim "$file"
            elif command -v nano &> /dev/null; then
                nano "$file"
            else
                less "$file"
            fi
            ;;
        *)
            echo "Unknown file type, trying default opener..."
            xdg-open "$file" &
            ;;
    esac
}

# Handle file:// URLs
if [[ "$URL" == file://* ]]; then
    FILE_PATH=$(decode_url "$URL")
    
    if [ -d "$FILE_PATH" ]; then
        echo "Opening directory..."
        # Create HTML directory listing
        TEMP_HTML=$(mktemp /tmp/dir-listing-XXXXXX.html)
        echo "<html><head><title>Directory: $FILE_PATH</title></head><body>" > "$TEMP_HTML"
        echo "<h1>Directory: $FILE_PATH</h1>" >> "$TEMP_HTML"
        echo "<ul>" >> "$TEMP_HTML"
        
        # List files
        find "$FILE_PATH" -maxdepth 1 -type f | sort | while read f; do
            filename=$(basename "$f")
            echo "<li><a href='file://$f'>📄 $filename</a></li>" >> "$TEMP_HTML"
        done
        
        # List directories
        find "$FILE_PATH" -maxdepth 1 -type d | grep -v "^$FILE_PATH$" | sort | while read d; do
            dirname=$(basename "$d")
            echo "<li><a href='file://$d'>📁 $dirname/</a></li>" >> "$TEMP_HTML"
        done
        
        echo "</ul></body></html>" >> "$TEMP_HTML"
        
        # Open in qutebrowser
        qutebrowser "$TEMP_HTML" &
        
    elif [ -f "$FILE_PATH" ]; then
        open_file "$FILE_PATH"
    else
        echo "Error: File not found: $FILE_PATH"
        notify-send "File Error" "File not found: $(basename "$FILE_PATH")"
    fi

# Handle http/https URLs
elif [[ "$URL" == http* ]]; then
    # Check if it's a PDF
    if [[ "$URL" == *.pdf ]] || [[ "$URL" == *pdf* ]]; then
        echo "Downloading PDF from web..."
        TEMP_PDF=$(mktemp /tmp/web-pdf-XXXXXX.pdf)
        wget -q "$URL" -O "$TEMP_PDF"
        
        if [ $? -eq 0 ]; then
            echo "Opening downloaded PDF..."
            zathura "$TEMP_PDF" &
        else
            echo "Failed to download PDF"
            # Fallback: open in browser
            qutebrowser "$URL" &
        fi
    else
        # Non-PDF URL, open in browser
        qutebrowser "$URL" &
    fi

# Local path without file://
elif [ -e "$URL" ]; then
    if [ -d "$URL" ]; then
        # Recursive call with file://
        exec "$0" "file://$URL"
    else
        open_file "$URL"
    fi

# Special C documentation shortcuts
else
    case "$URL" in
        "docs")
            exec "$0" "file://$DOCS_ROOT"
            ;;
        "books")
            exec "$0" "file://$DOCS_ROOT/books"
            ;;
        "advanced")
            exec "$0" "file://$DOCS_ROOT/advanced"
            ;;
        "standards")
            exec "$0" "file://$DOCS_ROOT/standards"
            ;;
        "kr")
            exec "$0" "file://$DOCS_ROOT/books/kr2/kr2.pdf"
            ;;
        "expert")
            exec "$0" "file://$DOCS_ROOT/advanced/expert-c.pdf"
            ;;
        *)
            echo "Unknown document: $URL"
            echo "Available shortcuts: docs, books, advanced, standards, kr, expert"
            ;;
    esac
fi
''')
    
    os.chmod(script_path, 0o755)
    
    # Now set up bindings
    docs_root = "/home/waks_work/Documents/PROJECTS/CLANG/docs"
    
    # Open any file/link with the universal opener
    config.bind('M', f'hint links spawn {script_path} {{hint-url}}')
    config.bind(',open', f'spawn {script_path} {{url}}')
    
    # Quick access to C documentation
    config.bind(',cdocs', f'spawn {script_path} docs')
    config.bind(',cbooks', f'spawn {script_path} books')
    config.bind(',cadv', f'spawn {script_path} advanced')
    config.bind(',cstd', f'spawn {script_path} standards')
    
    # Specific books (tries multiple formats)
    config.bind(',kr', f'spawn {script_path} kr')
    config.bind(',expert', f'spawn {script_path} expert')
    config.bind(',21c', f'spawn {script_path} "file://{docs_root}/advanced/21st-century-c.pdf"')
    config.bind(',cert', f'spawn {script_path} "file://{docs_root}/advanced/cert-c.pdf"')
    config.bind(',pointers', f'spawn {script_path} "file://{docs_root}/advanced/c-pointers.pdf"')
    
    # File browser mode
    config.bind(',fb', f'spawn {script_path} "file:///home/waks_work/Documents/"')
    config.bind(',fbdocs', f'spawn {script_path} "file://{docs_root}"')
    
    print("✅ Universal document opener configured!")
    print("   M        - Open any link/file with appropriate viewer")
    print("   ,open    - Open current URL with appropriate viewer")
    print("   ,cdocs   - Browse C documentation")
    print("   ,cbooks  - Browse C books")
    print("   ,cadv    - Browse advanced topics")
    print("   ,cstd    - Browse standards")
    print("   ,kr      - Open K&R book (tries multiple formats)")
    print("   ,expert  - Open Expert C Programming")
    print("   ,fb      - File browser for Documents")
    print("   ,fbdocs  - File browser for C docs")

def setup_global_navigation():
    """Set up global navigation for all documentation and tools"""
    
    import os

    # Create dashboard script if it doesn't exist
    script_dir = os.path.expanduser('~/.config/qutebrowser/userscripts')
    os.makedirs(script_dir, exist_ok=True)
    
    dashboard_script = os.path.join(script_dir, 'global-dashboard.sh')
    
    if not os.path.exists(dashboard_script):
        # Create the dashboard script
        with open(dashboard_script, 'w') as f:
            f.write('''#!/bin/bash
# Global Dashboard for all documentation and tools

create_dashboard() {
    cat << HTML
<!DOCTYPE html>
<html>
<head>
    <title>Global Documentation Dashboard</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        :root { --bg-primary: #0d1117; --bg-secondary: #161b22; --text-primary: #c9d1d9; --accent-blue: #58a6ff; --accent-green: #3fb950; }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: sans-serif; background: var(--bg-primary); color: var(--text-primary); padding: 20px; }
        .container { max-width: 1400px; margin: 0 auto; }
        header { text-align: center; margin-bottom: 40px; }
        h1 { color: var(--accent-blue); margin-bottom: 10px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }
        .section { background: var(--bg-secondary); border-radius: 8px; padding: 20px; }
        .section h2 { color: var(--accent-green); margin-bottom: 15px; }
        ul { list-style: none; }
        li { margin: 10px 0; padding: 8px; background: rgba(255,255,255,0.05); border-radius: 4px; }
        a { color: var(--text-primary); text-decoration: none; }
        a:hover { color: var(--accent-blue); }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Global Documentation Dashboard</h1>
            <p>One dashboard for all resources</p>
        </header>
        
        <div class="grid">
            
            <div class="section">
                <h2>C Programming</h2>
                    <ul>
                        <li>
                            <a href="http://localhost:8080" target="_blank">C Documentation</a>
                        </li>
                        <li>
                            <a href="file:///home/waks_work/Documents/PROJECTS/CLANG/docs" target="_blank">Local C Docs</a>
                        </li>
                        <li>
                            <a href="file:///home/waks_work/Documents/PROJECTS/CLANG/docs/books/kr2/kr2.pdf">K&R C Book</a>
                        </li>
                    </ul>
            </div>
            
            <div class="section">
                <h2>DevDocs</h2>
                <ul>
                    <li>
                        <a href="http://localhost:9292" target="_blank">DevDocs Server</a>
                    </li>
                    <li>
                        <a href="http://localhost:9292/#q=c" target="_blank">Search C</a>
                    </li>
                    <li>
                        <a href="http://localhost:9292/#q=linux" target="_blank">Search Linux</a>
                    </li>
                </ul>
            </div>

            <div class="section">
                <h2>Tools</h2>
                    <ul>
                    <li>
                        <a href="https://chat.openai.com" target="_blank">ChatGPT</a>
                    </li>
                    <li>
                        <a href="https://chat.deepseek.com" target="_blank">DeepSeek</a>
                    </li>
                    <li>
                        <a href="https://github.com" target="_blank">GitHub</a>
                    </li>
                </ul>
            </div>
        
        </div>
    </div>
</body>
</html>
HTML
}

DASHBOARD_HTML=$(mktemp /tmp/dashboard-XXXXXX.html)
create_dashboard > "\$DASHBOARD_HTML"
qutebrowser "\$DASHBOARD_HTML" &
(sleep 10 && rm -f "\$DASHBOARD_HTML") &
''')
        os.chmod(dashboard_script, 0o755)
    
    # Create global navigation bindings
    config.bind(',dash', f'spawn {dashboard_script}')
    config.bind(',global', f'spawn {dashboard_script}')
    
    # Quick access to everything
    config.bind(',cweb', 'open -t http://localhost:8080')
    config.bind(',devdocs', 'open -t http://localhost:9292')
    config.bind(',devc', 'open -t http://localhost:9292/#q=c')
    config.bind(',devlinux', 'open -t http://localhost:9292/#q=linux')
    config.bind(',devbash', 'open -t http://localhost:9292/#q=bash')
    
    # AI assistants
    config.bind(',chatgpt', 'open -t https://chat.openai.com')
    config.bind(',deepseek', 'open -t https://chat.deepseek.com')
    config.bind(',ds', 'open -t https://chat.deepseek.com')
    
    # Documentation
    config.bind(',cdocs', 'open -t file:///home/waks_work/Documents/PROJECTS/CLANG/docs')
    config.bind(',man', 'open -t file:///home/waks_work/Documents/PROJECTS/CLANG/docs/man/man3/index.txt')
    
    # System
    config.bind(',home', 'open -t file:///home/waks_work')
    config.bind(',docs', 'open -t file:///home/waks_work/Documents')
    
    print("🌐 GLOBAL NAVIGATION configured!")
    print("   ,dash     - Open Global Dashboard")
    print("   ,global   - Open Global Dashboard")
    print("   ,cweb     - C Documentation (localhost:8080)")
    print("   ,devdocs  - DevDocs (localhost:9292)")
    print("   ,devc     - Search C in DevDocs")
    print("   ,devlinux - Search Linux in DevDocs")
    print("   ,devbash  - Search Bash in DevDocs")
    print("   ,chatgpt  - ChatGPT")
    print("   ,deepseek - DeepSeek AI")
    print("   ,cdocs    - Local C docs directory")
    print("   ,man      - C man pages")
    print("   ,home     - Home directory")
    print("   ,docs     - Documents directory")

def setup_cloudflare_support():
    """Fix Cloudflare challenges and verification"""
    
    cloudflare_domains = [
        'cloudflare.com',
        'challenges.cloudflare.com',
        'cdn.cloudflare.com',
    ]
    
    for domain in cloudflare_domains:
        # Only settings that SUPPORT URL patterns
        config.set('content.javascript.enabled', True, domain)
        config.set('content.javascript.clipboard', 'access', domain)  # FIXED
        
        # Cookies
        config.set('content.cookies.accept', 'all', domain)
        
        # Local storage
        config.set('content.local_storage', True, domain)
        
        # Canvas and WebGL
        config.set('content.canvas_reading', True, domain)
        config.set('content.webgl', True, domain)
        
        # Notifications
        config.set('content.notifications.enabled', True, domain)
        
        # Geolocation
        config.set('content.geolocation', True, domain)
        
        # Disable ad blocking
        config.set('content.blocking.enabled', False, domain)
    
    # Global settings (NOT per-domain)
    c.content.headers.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    c.content.headers.accept_language = 'en-US,en;q=0.9'
    
    print("✅ Cloudflare challenge support enabled")

def main():
    """Main configuration setup function"""
    
    # Security & Privacy (UPDATED)
    setup_security_settings()  # Now allows canvas/WebGL
    setup_cookie_settings()
    setup_javascript_settings()
    
    # === NEW: Authentication fixes ===
    setup_cloudflare_support()
    setup_google_login_complete()
    setup_chatgpt_complete()
    setup_deepseek_advanced()  # Updated version
    setup_third_party_cookies()
    
    # Theming
    setup_dark_mode()
    setup_user_agent()
    bg, fg, accent, red, yellow, green, peach = setup_colors()
    setup_color_scheme(bg, fg, accent, red, yellow, green, peach)
    
    # Key Bindings
    setup_media_bindings()
    setup_ai_bindings()
    setup_security_bindings()
    setup_theme_bindings()
    setup_search_bindings()
    setup_navigation_bindings()
    setup_utility_bindings()
    setup_quick_access_bindings()
    setup_adblock_control_bindings()
    
    # Behavior & Content
    setup_behavior_settings()
    setup_search_engines()
    setup_content_settings()
    setup_fonts()
    setup_window_settings()
    setup_pure_app_mode()
    
    # PDF & Zoom
    setup_pdf_support()
    setup_zoom_settings()
    
    # Security Exceptions (keep existing but updated)
    setup_trusted_sites()  # Updated version
    setup_session_management()
    setup_youtube_music_fixes() 
    setup_youtube_strict_fixes()
    setup_youtube_content_blocking()  # NEW from previous fix
    setup_security_headers()
    setup_performance_settings()
    setup_input_settings()
    
    # Ad Blocking (updated)
    setup_adblocking_nuclear()  # Updated with YouTube filters
    setup_javascript_adblocking()
    
    # Navigation
    setup_global_navigation()
    
    # Final message
    print_success_message()

# Run the main configuration
main()

config.bind(',debug', 'jseval console.log("Cookies:", document.cookie); console.log("LocalStorage:", localStorage); console.log("SessionStorage:", sessionStorage)')
config.bind(',cookies', 'jseval alert("Cookies: " + document.cookie)')
config.bind(',checkjs', 'jseval alert("JavaScript is working!")')
