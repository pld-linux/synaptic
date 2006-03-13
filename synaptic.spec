#
# Conditional build:
%bcond_without	doc	# build documentation
#
Summary:	Graphical package management program for apt
Name:		synaptic
Version:	0.57.2
Release:	0.3
License:	GPL
Group:		Applications/Archiving
Source0:	http://download.savannah.nongnu.org/releases/synaptic/%{name}-%{version}.tar.gz
# Source0-md5:	dd753e953caa053279d342e3bc269128
URL:		http://www.nongnu.org/synaptic/
BuildRequires:	XFree86-devel
BuildRequires:	apt-devel >= 0.5.5
BuildRequires:	atk-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libart_lgpl-devel
BuildRequires:	libglade2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel
BuildRequires:	libzvt-devel
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm-devel >= 4.1
BuildRequires:	scrollkeeper
%{?with_doc:BuildRequires:	xmlto}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Synaptic is a graphical package management program for apt. It
provides the same features as the apt-get command line utility with a
GUI front-end based on Gtk+.

Features:
- Install, remove, upgrade and downgrade single and multiple packages.
- Upgrade your whole system.
- Manage package repositories (sources.list).
- Find packages by name, description and several other attributes.
- Select packages by status, section, name or a custom filter.
- Sort packages by name, status, size or version.
- Browse all available online documentation related to a package.
- Download the latest changelog of a package.
- Lock packages to the current version.
- Force the installation of a specifc package version.
- Undo/Redo of selections.
- Built-in terminal emulator for the package manager.
- Debian only: Configure packages through the debconf system.

%prep
%setup -q

%build
%configure \
  --with-zvt \
  %{?with_doc:--enable-docdir=%{_defaultdocdir}}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS INSTALL NEWS README TODO
/etc/X11/sysconfig/synaptic.desktop
%attr(755,root,root) %{_sbindir}/synaptic
%{_desktopdir}/synaptic-kde.desktop
%{_desktopdir}/synaptic.desktop
%dir %{_datadir}/gnome/help/synaptic
%{_datadir}/gnome/help/synaptic/C
%lang(es) %{_datadir}/gnome/help/synaptic/es
%{_mandir}/man8/synaptic.8*
%{_datadir}/omf/synaptic/synaptic-C.omf
%lang(es) %{_datadir}/omf/synaptic/synaptic-es.omf
%{_pixmapsdir}/synaptic.png
%{_datadir}/synaptic/glade
%{_datadir}/synaptic/html
%{_datadir}/synaptic/pixmaps
