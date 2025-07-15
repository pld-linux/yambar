Summary:	Modular status panel for X11 and Wayland
Name:		yambar
Version:	1.11.0
Release:	1
License:	MIT
Group:		Applications
Source0:	https://codeberg.org/dnkl/yambar/archive/%{version}.tar.gz
# Source0-md5:	2cd1725479977b4132bdba8d3d3458de
URL:		https://codeberg.org/dnkl/yambar/
BuildRequires:	alsa-lib-devel
BuildRequires:	bison
BuildRequires:	fcft-devel < 4.0.0
BuildRequires:	fcft-devel >= 3.0.0
BuildRequires:	flex
BuildRequires:	json-c-devel
BuildRequires:	libmpdclient-devel
BuildRequires:	libxcb-devel
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja
BuildRequires:	pipewire-devel >= 0.3
BuildRequires:	pixman-devel
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	scdoc
BuildRequires:	tllist-devel >= 1.0.1
BuildRequires:	udev-devel
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols
BuildRequires:	xcb-util-cursor-devel
BuildRequires:	xcb-util-devel
BuildRequires:	xcb-util-errors-devel
BuildRequires:	xcb-util-wm-devel
BuildRequires:	yaml-devel
Requires(post,postun):	desktop-file-utils
Requires:	fcft < 4.0.0
Requires:	fcft >= 3.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-Wno-format-truncation

%description
yambar is a lightweight and configurable status panel (bar, for short)
for X11 and Wayland, that goes to great lengths to be both CPU and
battery efficient - polling is only done when absolutely necessary.

%package devel
Summary:	Header files for yambar
Group:		Development/Libraries

%description devel
Header files for yambar.

%package -n zsh-completion-yambar
Summary:	ZSH completion for yambar command line
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	zsh
BuildArch:	noarch

%description -n zsh-completion-yambar
ZSH completion for yambar command line.

%prep
%setup -q -n %{name}

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md
%attr(755,root,root) %{_bindir}/yambar
%{_desktopdir}/yambar.desktop
%{_mandir}/man1/yambar.1*
%{_mandir}/man5/yambar.5*
%{_mandir}/man5/yambar-decorations.5*
%{_mandir}/man5/yambar-modules*.5*
%{_mandir}/man5/yambar-particles.5*
%{_mandir}/man5/yambar-tags.5*

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/yambar
%{_includedir}/yambar/*.h
%dir %{_includedir}/yambar/bar
%{_includedir}/yambar/bar/*.h

%files -n zsh-completion-yambar
%defattr(644,root,root,755)
%{zsh_compdir}/_yambar
