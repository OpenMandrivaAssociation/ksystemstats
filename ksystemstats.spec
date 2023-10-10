%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Name: ksystemstats
Version: 5.27.8
Release: 2
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Summary: Collect statistics about the running Plasma
URL: http://kde.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5Solid)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5NetworkManagerQt)
BuildRequires: cmake(KF5SysGuard)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(udev)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(libnl-3.0)
BuildRequires: pkgconfig(libpcap)
BuildRequires: lm_sensors-devel
BuildConflicts: plasma6-xdg-desktop-portal-kde

%description
KSystemStats is a daemon that collects
statistics about the running system.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%{_bindir}/%{name}
%{_bindir}/kstatsviewer
%dir %{_qt5_plugindir}/%{name}
%{_qt5_plugindir}/%{name}/*.so
%{_userunitdir}/plasma-%{name}.service
%{_datadir}/dbus-1/services/*.%{name}.service
