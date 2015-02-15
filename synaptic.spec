#
# Conditional build:
%bcond_without	doc	# build documentation
#
Summary:	Graphical package management program for apt
Summary(pl.UTF-8):	Graficzny program do zarządzania pakietami dla apta
Name:		synaptic
Version:	0.57.2
Release:	0.3
License:	GPL v2+
Group:		Applications/Archiving
Source0:	http://download.savannah.nongnu.org/releases/synaptic/%{name}-%{version}.tar.gz
# Source0-md5:	dd753e953caa053279d342e3bc269128
# http://apt-rpm.org/patches/synaptic-0.57.2-gcc41.patch
Patch0:		%{name}-gcc.patch
# http://apt-rpm.org/patches/synaptic-0.57.2-progressapi-hack.patch
Patch1:		%{name}-progressapi-hack.patch
# http://apt-rpm.org/patches/synaptic-0.57.2-repomd-1.patch
Patch2:		%{name}-repomd.patch
# http://apt-rpm.org/patches/synaptic-0.57.2-showprog.patch
Patch3:		%{name}-showprog.patch
Patch4:		%{name}-format.patch
Patch5:		%{name}-includes.patch
URL:		http://www.nongnu.org/synaptic/
BuildRequires:	apt-devel >= 0.5.5
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	intltool >= 0.23
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	pango-devel >= 1:1.0.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-devel >= 4.1
BuildRequires:	scrollkeeper
BuildRequires:	vte0-devel >= 0.10.11
%{?with_doc:BuildRequires:	xmlto}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Synaptic is a graphical package management program for apt. It
provides the same features as the apt-get command line utility with a
GUI front-end based on GTK+.

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
- Force the installation of a specific package version.
- Undo/Redo of selections.
- Built-in terminal emulator for the package manager.
- Debian only: Configure packages through the debconf system.

%description -l pl.UTF-8
Synaptic to graficzny program do zarządzania pakietami dla programu
apt. Udostępnia te same możliwości, co narzędzie linii poleceń
apt-get, ale z graficznym interfejsem użytkownika opartym na GTK+.

Możliwości:
- instalacja, usuwanie, aktualizacja i cofanie pojedynczych lub wielu
  pakietów
- aktualizacja całego systemu
- zarządzanie repozytoriami pakietów (sources.list)
- wyszukiwanie pakietów po nazwie, opisie i kilku innych atrybutach
- wybór pakietów według statusu, sekcji, nazwy lub własnego filtra
- sortowanie pakietów po nazwie, statusie, rozmiarze lub wersji
- przeglądanie całej dostępnej dokumentacji związanej z pakietem
- pobieranie najnowszej listy zmian pakietu
- blokowanie pakietów do obecnej wersji
- wymuszanie instalacji określonej wersji pakietu
- anulowanie/powtarzanie wyboru
- wbudowany emulator terminala dla zarządcy pakietów
- (tylko Debian) konfigurowanie pakietów przez system debconf

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%configure \
	--with-vte \
	%{?with_doc:--enable-docdir=%{_docdir}}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT/etc/X11/sysconfig/synaptic.desktop

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README README.supported README.tasks TODO TRANSLATORS
%attr(755,root,root) %{_sbindir}/synaptic
%{_desktopdir}/synaptic-kde.desktop
%{_desktopdir}/synaptic.desktop
%{_mandir}/man8/synaptic.8*
%{_pixmapsdir}/synaptic.png
%dir %{_datadir}/synaptic
%{_datadir}/synaptic/glade
%{_datadir}/synaptic/html
%{_datadir}/synaptic/pixmaps
