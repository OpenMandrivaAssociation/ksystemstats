%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Name: ksystemstats
Version:	6.4.2
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/ksystemstats/-/archive/%{gitbranch}/ksystemstats-%{gitbranchd}.tar.bz2#/ksystemstats-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/ksystemstats-%{version}.tar.xz
%endif
Summary: KDE Frameworks 6 system monitoring framework
URL: https://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6CoreTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6WebEngineCore)
BuildRequires: cmake(Qt6WebEngineWidgets)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6WidgetsTools)
BuildRequires: cmake(Qt6Positioning)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(zlib)
BuildRequires: cmake(Qt6Designer)
BuildRequires: cmake(Qt6Sensors)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KSysGuard) >= 5.27.80
BuildRequires: cmake(Plasma) >= 5.90.0
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6Auth)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6NetworkManagerQt)
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(libnm) >= 1.4.0
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(libnl-3.0)
BuildRequires: pkgconfig(libpcap)
BuildRequires: pkgconfig(libcap)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libdrm)
BuildRequires: lm_sensors-devel
BuildSystem: cmake
BuildOption: -DBUILD_QCH:BOOL=ON
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
# Renamed after 6.0 2025-05-01
%rename plasma6-ksystemstats

%description
KDE Frameworks 6 system monitoring framework.

%files -f %{name}.lang
%{_prefix}/lib/systemd/user/plasma-ksystemstats.service
%{_bindir}/ksystemstats
%{_bindir}/kstatsviewer
%{_qtdir}/plugins/ksystemstats
%{_datadir}/dbus-1/services/org.kde.ksystemstats1.service
%{_datadir}/qlogging-categories6/ksystemstats.categories
%{_libdir}/libexec/ksystemstats_intel_helper
