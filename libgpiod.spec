# TODO:
# - rust bindings (--enable-bindings-rust, needs vendoring; BR: cargo, rust)
# - tests (BR: kmod-devel >= 18, libmount-devel >= 2.33.1, glib2-devel >= 1:2.50 for library; bats for tools; catch2 for C++)
#
# Conditional build:
%bcond_without	apidocs		# Doxygen API documentation
%bcond_without	python		# Python binding
%bcond_without	static_libs	# static libraries
#
Summary:	Library for interacting with the Linux GPIO character device
Summary(pl.UTF-8):	Biblioteka do obsługi linuksowych urządzeń znakowych GPIO
Name:		libgpiod
Version:	2.2.1
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://www.kernel.org/pub/software/libs/libgpiod/%{name}-%{version}.tar.xz
# Source0-md5:	96111292f46e2a646cd9dd8802a0c3a4
Patch0:		%{name}-python.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-docs.patch
URL:		https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/
BuildRequires:	autoconf >= 2.71
BuildRequires:	autoconf-archive
BuildRequires:	automake
%{?with_apidocs:BuildRequires:	doxygen}
# docs not installed as of 2.2
#BuildRequires:	gi-docgen
BuildRequires:	glib2-devel >= 1:2.80
BuildRequires:	gobject-introspection-devel >= 0.6.2
BuildRequires:	help2man
BuildRequires:	libedit-devel >= 3.1
BuildRequires:	libgudev-devel >= 230
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	libtool >= 2:2
BuildRequires:	linux-libc-headers >= 7:5.5
%{?with_apidocs:BuildRequires:	pandoc}
BuildRequires:	pkgconfig >= 1:0.28
%if %{with python}
BuildRequires:	python3 >= 1:3.9
BuildRequires:	python3-devel >= 1:3.9
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	python3-setuptools
%endif
%{?with_apidocs:BuildRequires:	sphinx-pdg}
BuildRequires:	rpm-build >= 4.6
BuildRequires:	systemd-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Since Linux 4.8 the GPIO sysfs interface is deprecated. User space
should use the character device instead. This library encapsulates the
ioctl calls and data structures behind a straightforward API.

%description -l pl.UTF-8
Od wersja Linuksa 4.8 interfejs sysfs do GPIO jest przestarzały.
Przestrzeń użytkownika powinna zamiast niego używać urządzenia
znakowego. Ta biblioteka kryje wywołania ioctl i struktury danych za
bezpośrednim API.

%package devel
Summary:	Header files for libgpiod library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgpiod
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libgpiod library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgpiod.

%package static
Summary:	Static libgpiod library
Summary(pl.UTF-8):	Statyczna biblioteka libgpiod
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgpiod library.

%description static -l pl.UTF-8
Statyczna biblioteka libgpiod.

%package cxx
Summary:	C++ binding for libgpiod library
Summary(pl.UTF-8):	Interfejs C++ do biblioteki libgpiod
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description cxx
High-level, object-oriented C++ binding for libgpiod library.

%description cxx -l pl.UTF-8
Wysokopoziomowy, zorientowany obiektowo interfejs C++ do biblioteki
libgpiod.

%package cxx-devel
Summary:	Header files for libgpiodcxx library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgpiodcxx
Group:		Development/Libraries
Requires:	%{name}-cxx = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libstdc++-devel >= 6:7

%description cxx-devel
Header files for libgpiodcxx library.

%description cxx-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgpiodcxx.

%package cxx-static
Summary:	Static libgpiodcxx library
Summary(pl.UTF-8):	Statyczna biblioteka libgpiodcxx
Group:		Development/Libraries
Requires:	%{name}-cxx-devel = %{version}-%{release}

%description cxx-static
Static libgpiodcxx library.

%description cxx-static -l pl.UTF-8
Statyczna biblioteka libgpiodcxx.

%package glib
Summary:	GObject bindings for libgpiod library
Summary(pl.UTF-8):	Interfejs GObject do biblioteki libgpiod
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2 >= 1:2.80

%description glib
GObject bindings for libgpiod library.

%description glib -l pl.UTF-8
Interfejs GObject do biblioteki libgpiod.

%package glib-devel
Summary:	Header files for libgpiod-glib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgpiod-glib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-glib = %{version}-%{release}
Requires:	glib2-devel >= 1:2.80

%description glib-devel
Header files for libgpiod-glib library.

%description glib-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgpiod-glib.

%package glib-static
Summary:	Static libgpiod-glib library
Summary(pl.UTF-8):	Statyczna biblioteka libgpiod-glib
Group:		Development/Libraries
Requires:	%{name}-glib-devel = %{version}-%{release}

%description glib-static
Static libgpiod-glib library.

%description glib-static -l pl.UTF-8
Statyczna biblioteka libgpiod-glib.

%package dbus
Summary:	DBus library and daemon
Summary(pl.UTF-8):	Biblioteka i demon DBus
Group:		Libraries
Requires:	glib2 >= 1:2.80
Requires:	libgudev >= 230

%description dbus
DBus library and daemon.

%description dbus -l pl.UTF-8
Biblioteka i demon DBus.

%package dbus-devel
Summary:	Header files for gpiodbus library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gpiodbus
Group:		Development/Libraries
Requires:	%{name}-dbus = %{version}-%{release}
Requires:	glib2-devel >= 1:2.80

%description dbus-devel
Header files for gpiodbus library.

%description dbus-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gpiodbus.

%package dbus-static
Summary:	Static gpiodbus library
Summary(pl.UTF-8):	Statyczna biblioteka gpiodbus
Group:		Development/Libraries
Requires:	%{name}-dbus-devel = %{version}-%{release}

%description dbus-static
Static gpiodbus library.

%description dbus-static -l pl.UTF-8
Statyczna biblioteka gpiodbus.

%package tools
Summary:	Tools for interacting with the Linux GPIO character device
Summary(pl.UTF-8):	Narzędzia do obsługi linuksowych urządzeń znakowych GPIO
Group:		Application/System
Requires:	%{name} = %{version}-%{release}

%description tools
Tools for interacting with the Linux GPIO character device.

%description tools -l pl.UTF-8
Narzędzia do obsługi linuksowych urządzeń znakowych GPIO.

%package -n python3-gpiod
Summary:	Pythona binding for libgpiod library
Summary(pl.UTF-8):	Interfejs Pythona do biblioteki libgpiod
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python3-gpiod
High-level, object-oriented Python binding for libgpiod library.

%description -n python3-gpiod -l pl.UTF-8
Wysokopoziomowy, zorientowany obiektowo interfejs Pythona do
biblioteki libgpiod.

%package apidocs
Summary:	API documentation for libgpiod library
Summary(pl.UTF-8):	Dokumentacja API biblioteki libgpiod
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for libgpiod library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libgpiod.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static} \
	--enable-bindings-cxx \
	--enable-bindings-glib \
	%{?with_python:--enable-bindings-python} \
	--enable-dbus \
	--enable-gpioset-interactive \
	--disable-silent-rules \
	--enable-systemd \
	--enable-tools
%{__make}

%if %{with apidocs}
%{__make} docs \
	SHELL=bash
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	udevdir=/lib/udev/rules.d

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgpiod*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	cxx -p /sbin/ldconfig
%postun	cxx -p /sbin/ldconfig

%post	dbus -p /sbin/ldconfig
%postun	dbus -p /sbin/ldconfig

%post	glib -p /sbin/ldconfig
%postun	glib -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_libdir}/libgpiod.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgpiod.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgpiod.so
%{_includedir}/gpiod.h
%{_pkgconfigdir}/libgpiod.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgpiod.a
%endif

%files cxx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgpiodcxx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgpiodcxx.so.2

%files cxx-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgpiodcxx.so
%{_includedir}/gpiod.hpp
%{_includedir}/gpiodcxx
%{_pkgconfigdir}/libgpiodcxx.pc

%if %{with static_libs}
%files cxx-static
%defattr(644,root,root,755)
%{_libdir}/libgpiodcxx.a
%endif

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gpiodetect
%attr(755,root,root) %{_bindir}/gpioget
%attr(755,root,root) %{_bindir}/gpioinfo
%attr(755,root,root) %{_bindir}/gpiomon
%attr(755,root,root) %{_bindir}/gpionotify
%attr(755,root,root) %{_bindir}/gpioset
%{_mandir}/man1/gpiodetect.1*
%{_mandir}/man1/gpioget.1*
%{_mandir}/man1/gpioinfo.1*
%{_mandir}/man1/gpiomon.1*
%{_mandir}/man1/gpionotify.1*
%{_mandir}/man1/gpioset.1*

%if %{with python}
%files -n python3-gpiod
%defattr(644,root,root,755)
%dir %{py3_sitedir}/gpiod
%attr(755,root,root) %{py3_sitedir}/gpiod/_ext.cpython-*.so
%{py3_sitedir}/gpiod/*.py
%{py3_sitedir}/gpiod/__pycache__
%{py3_sitedir}/gpiod-2.2.0-py*.egg-info
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc docs/doxygen-output/html/*
%endif

%files glib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgpiod-glib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgpiod-glib.so.1
%{_libdir}/girepository-1.0/Gpiodglib-1.0.typelib

%files glib-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgpiod-glib.so
%{_includedir}/gpiod-glib
%{_includedir}/gpiod-glib.h
%{_datadir}/gir-1.0/Gpiodglib-1.0.gir
%{_pkgconfigdir}/gpiod-glib.pc

%if %{with static_libs}
%files glib-static
%defattr(644,root,root,755)
%{_libdir}/libgpiod-glib.a
%endif

%files dbus
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gpio-manager
%attr(755,root,root) %{_bindir}/gpiocli
%attr(755,root,root) %{_libdir}/libgpiodbus.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgpiodbus.so.1
/etc/dbus-1/system.d/io.gpiod1.conf
/lib/udev/rules.d/90-gpio.rules
%{_datadir}/dbus-1/interfaces/io.gpiod1.xml
%{systemdunitdir}/gpio-manager.service
%{_mandir}/man1/gpio-manager.1*
%{_mandir}/man1/gpiocli*.1*

%files dbus-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgpiodbus.so
%{_includedir}/generated-gpiodbus.h
%{_includedir}/gpiodbus.h

%if %{with static_libs}
%files dbus-static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgpiodbus.a
%endif
