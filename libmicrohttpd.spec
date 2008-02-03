%define major 3
%define shortname microhttpd
%define libname	%mklibname %shortname %major
%define develname %mklibname -d %shortname
%define sdevelname %mklibname -d -s %shortname

Name:		libmicrohttpd
Version:	0.2.1
Release:	%mkrel 1
URL:		http://gnunet.org/libmicrohttpd/
Source:		http://gnunet.org/libmicrohttpd/download/%{name}-%{version}.tar.gz
License:	GPLv2+
Summary:	Small C library to run an HTTP server
Group:		System/Libraries
BuildRequires:	libcurl-devel
%description
libmicrohttpd is a small C library that is supposed to make it easy to
run an HTTP server as part of another application. Key features that
distinguish libmicrohttpd from other projects are:

	* C library: fast and small
	* API is simple, expressive and fully reentrant
	* Implementation is (largely) http 1.1 compliant
	* HTTP server can listen on multiple ports
	* Support for IPv6
	* Creates binary of only 22k (for now)
	* Three different threading models

libmicrohttpd was started because the author needed an easy way to add
a concurrent HTTP server to other projects. Existing alternatives were
either non-free, not reentrant, standalone, of terrible code quality or
a combination thereof. Do not use libmicrohttpd if you are looking for
a standalone http server, there are many other projects out there that
provide that kind of functionality already. However, if you want to be
able to serve simple WWW pages from within your C or C++ application,
check it out.

%package -n %libname
Summary:	Small C library to run an HTTP server
Group:		System/Libraries

%description -n %libname
libmicrohttpd is a small C library that is supposed to make it easy to
run an HTTP server as part of another application. Key features that
distinguish libmicrohttpd from other projects are:

	* C library: fast and small
	* API is simple, expressive and fully reentrant
	* Implementation is (largely) http 1.1 compliant
	* HTTP server can listen on multiple ports
	* Support for IPv6
	* Creates binary of only 22k (for now)
	* Three different threading models

libmicrohttpd was started because the author needed an easy way to add
a concurrent HTTP server to other projects. Existing alternatives were
either non-free, not reentrant, standalone, of terrible code quality or
a combination thereof. Do not use libmicrohttpd if you are looking for
a standalone http server, there are many other projects out there that
provide that kind of functionality already. However, if you want to be
able to serve simple WWW pages from within your C or C++ application,
check it out.

%package -n %develname
Summary:	Development files for %libname
Group:		System/Libraries
Provides:	%name-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
%description -n %develname
Development files for %libname

%package -n %sdevelname
Summary:	Static libraries for %libname
Group:		System/Libraries
Provides:	%name-static-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	%{develname} = %{version}-%{release}
%description -n %sdevelname
Static libraries for %libname

%prep
%setup -q

%build
%configure
# makefile doesn't support running multiple jobs simultaneously
%{__make}

%install
%{__rm} -Rf %{buildroot}
%makeinstall

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/%{name}.so.%{major}*
%{_mandir}/man3/%{name}.3.*

%files -n %develname
%{_includedir}/%{shortname}.h
%{_libdir}/%{name}.so
%{_libdir}/%{name}.la

%files -n %sdevelname
%{_libdir}/%{name}.a

