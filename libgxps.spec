Summary:	XPS documents library
Summary(pl.UTF-8):	Biblioteka do obsługi dokumentów XPS
Name:		libgxps
Version:	0.2.2
Release:	3
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgxps/0.2/%{name}-%{version}.tar.xz
# Source0-md5:	65bec2033ff71307f429dc3f91d60233
URL:		http://live.gnome.org/libgxps
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.10
BuildRequires:	cairo-devel >= 1.10.0
BuildRequires:	freetype-devel
BuildRequires:	glib2-devel >= 1:2.24.0
BuildRequires:	gnome-common
BuildRequires:	gobject-introspection-devel >= 0.10.1
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	lcms2-devel
BuildRequires:	libarchive-devel >= 2.8.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	cairo >= 1.10.0
Requires:	glib2 >= 1:2.24.0
Requires:	libarchive >= 2.8.0
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
Requires:	glib2-devel >= 1:2.24.0
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

%description apidocs
API documentation for libgxps library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libgxps.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir} \
	--enable-gtk-doc \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/xpstojpeg
%attr(755,root,root) %{_bindir}/xpstopdf
%attr(755,root,root) %{_bindir}/xpstopng
%attr(755,root,root) %{_bindir}/xpstops
%attr(755,root,root) %{_bindir}/xpstosvg
%attr(755,root,root) %{_libdir}/libgxps.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgxps.so.2
%{_libdir}/girepository-1.0/GXPS-0.1.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgxps.so
%{_datadir}/gir-1.0/GXPS-0.1.gir
%{_includedir}/libgxps
%{_pkgconfigdir}/libgxps.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgxps.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libgxps
