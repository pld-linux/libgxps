Summary:	XPS documents library
Name:		libgxps
Version:	0.1.0
Release:	1
License:	LGPL v2
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgxps/0.1/%{name}-%{version}.tar.xz
# Source0-md5:	90f5a678c23a98256d921af659eb204a
URL:		http://live.gnome.org/libgxps
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.10
BuildRequires:	cairo-devel >= 1.10.0
BuildRequires:	freetype-devel
BuildRequires:	glib2-devel >= 1:2.24.0
BuildRequires:	gnome-common
BuildRequires:	gobject-introspection-devel >= 0.10.1
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	libarchive-devel >= 2.8.0
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgxps is a GObject based library for handling and rendering XPS
documents.

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
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libgxps.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgxps.so.1
%{_libdir}/girepository-1.0/GXPS-0.1.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgxps.so
%{_datadir}/gir-1.0/GXPS-0.1.gir
%{_includedir}/libgxps
%{_pkgconfigdir}/libgxps.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libgxps
