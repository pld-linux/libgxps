#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	XPS documents library
Summary(pl.UTF-8):	Biblioteka do obsługi dokumentów XPS
Name:		libgxps
Version:	0.3.2
Release:	3
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://download.gnome.org/sources/libgxps/0.3/%{name}-%{version}.tar.xz
# Source0-md5:	0527ac7c8c405445e96a5baa6019a0c3
URL:		https://wiki.gnome.org/Projects/libgxps
BuildRequires:	cairo-devel >= 1.10.0
BuildRequires:	freetype-devel >= 2
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	gobject-introspection-devel >= 0.10.1
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	lcms2-devel >= 2
BuildRequires:	libarchive-devel >= 2.8.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel >= 4
BuildRequires:	libxslt-progs
BuildRequires:	meson >= 0.43.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	cairo >= 1.10.0
Requires:	glib2 >= 1:2.36.0
Requires:	libarchive >= 2.8.0
Requires:	libtiff >= 4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgxps is a GObject based library for handling and rendering XPS
documents.

%description -l pl.UTF-8
libgxps to oparta na szkielecie GObject biblioteka do obsługi i
renderowania dokumentów XPS.

%package devel
Summary:	Header files for libgxps library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgxps
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo-devel >= 1.10.0
Requires:	glib2-devel >= 1:2.36.0
Requires:	libarchive-devel >= 2.8.0

%description devel
Header files for libgxps library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgxps.

%package static
Summary:	Static libgxps libary
Summary(pl.UTF-8):	Statyczna biblioteka libgxps
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgxps libary.

%description static -l pl.UTF-8
Statyczna biblioteka libgxps.

%package apidocs
Summary:	libgxps API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libgxps
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
API documentation for libgxps library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libgxps.

%prep
%setup -q

%if %{with static_libs}
%{__sed} -i -e 's/shared_library/library/' libgxps/meson.build
%endif

%build
%meson \
	-Denable-gtk-doc=true \
	-Denable-man=true \
	-Denable-test=false

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README TODO
%attr(755,root,root) %{_bindir}/xpstojpeg
%attr(755,root,root) %{_bindir}/xpstopdf
%attr(755,root,root) %{_bindir}/xpstopng
%attr(755,root,root) %{_bindir}/xpstops
%attr(755,root,root) %{_bindir}/xpstosvg
%attr(755,root,root) %{_libdir}/libgxps.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgxps.so.2
%{_libdir}/girepository-1.0/GXPS-0.1.typelib
%{_mandir}/man1/xpstojpeg.1*
%{_mandir}/man1/xpstopdf.1*
%{_mandir}/man1/xpstopng.1*
%{_mandir}/man1/xpstops.1*
%{_mandir}/man1/xpstosvg.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgxps.so
%{_datadir}/gir-1.0/GXPS-0.1.gir
%{_includedir}/libgxps
%{_pkgconfigdir}/libgxps.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgxps.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libgxps
