# TODO: tests (BR: kmod-devel >= 18, udev-devel >= 1:215, glib2-devel >= 1:2.50 for library; bats for tools; catch2 for C++)
#
# Conditional build:
%bcond_without	apidocs		# Doxygen API documentation
%bcond_without	python		# Python binding
%bcond_without	static_libs	# static libraries
#
Summary:	Library and tools for interacting with the Linux GPIO character device
Summary(pl.UTF-8):	Biblioteka i narzędzia do obsługi linuksowych urządzeń znakowych GPIO
Name:		libgpiod
Version:	1.6.3
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://www.kernel.org/pub/software/libs/libgpiod/%{name}-%{version}.tar.xz
# Source0-md5:	28e79f6f70fee1da9079558d8b7b3736
URL:		https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	help2man
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	linux-libc-headers >= 6:5.5
%{?with_python:BuildRequires:	python3-devel >= 1:3.2}
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
Requires:	libstdc++-devel >= 6:4.7

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

%build
%configure \
	%{!?with_static_libs:--disable-static} \
	--enable-bindings-cxx \
	%{?with_python:--enable-bindings-python} \
	--disable-silent-rules \
	--enable-tools
%{__make}

%if %{with apidocs}
%{__make} doc
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgpiod*.la
%if %{with python}
%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/gpiod.la \
	%{?with_static_libs:$RPM_BUILD_ROOT%{py3_sitedir}/gpiod.a}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	cxx -p /sbin/ldconfig
%postun	cxx -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/gpiodetect
%attr(755,root,root) %{_bindir}/gpiofind
%attr(755,root,root) %{_bindir}/gpioget
%attr(755,root,root) %{_bindir}/gpioinfo
%attr(755,root,root) %{_bindir}/gpiomon
%attr(755,root,root) %{_bindir}/gpioset
%attr(755,root,root) %{_libdir}/libgpiod.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgpiod.so.2
%{_mandir}/man1/gpiodetect.1*
%{_mandir}/man1/gpiofind.1*
%{_mandir}/man1/gpioget.1*
%{_mandir}/man1/gpioinfo.1*
%{_mandir}/man1/gpiomon.1*
%{_mandir}/man1/gpioset.1*

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
%attr(755,root,root) %ghost %{_libdir}/libgpiodcxx.so.1

%files cxx-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgpiodcxx.so
%{_includedir}/gpiod.hpp
%{_pkgconfigdir}/libgpiodcxx.pc

%if %{with static_libs}
%files cxx-static
%defattr(644,root,root,755)
%{_libdir}/libgpiodcxx.a
%endif

%if %{with python}
%files -n python3-gpiod
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/gpiod.so
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc doc/html/*
%endif
