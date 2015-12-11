%define sname microhttpd
%define major 12
%define libname %mklibname %{sname} %major
%define devname %mklibname -d %{sname}
%define spdymajor 0
%define libspdy %mklibname microspdy %spdymajor

Summary:	Small C library to run an HTTP server
Name:		libmicrohttpd
Version:	0.9.47
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		http://gnunet.org/libmicrohttpd/
Source0:	http://ftp.gnu.org/gnu/libmicrohttpd/%{name}-%{version}.tar.gz
Patch0:		libmicrohttpd-0.9.35-link.patch
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libgcrypt)

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
a standalone http server; there are many other projects out there that
provide that kind of functionality already. However, if you want to be
able to serve simple WWW pages from within your C or C++ application,
check it out.

%package -n %{libname}
Summary:	Small C library to run an HTTP server
Group:		System/Libraries

%description -n %{libname}
libmicrohttpd is a small C library that is supposed to make it easy to
run an HTTP server as part of another application. Key features that
distinguish libmicrohttpd from other projects are:

%package -n %libspdy
Summary:	API of SPDY server
Group:		System/Libraries

%description -n %libspdy
libmicrospdy provides a compact API of SPDY server. libmicrospdy currently
only implements version 3 of SPDY and accepts only TLS connections.

%package -n	microspdy2http
Summary:	Implementation of SPDY server
Group:		System/Base

%description -n microspdy2http
microspdy2http provides an implementation of SPDY server.


%package -n %{devname}
Summary:	Development files for %{libname}
Group:		System/Libraries
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libspdy} = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Development files for %{libname}

%prep
%setup -q

%build
%configure --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

%files -n microspdy2http
%{_bindir}/microspdy2http

%files -n %{libspdy}
%{_libdir}/libmicrospdy.so.%{spdymajor}
%{_libdir}/libmicrospdy.so.%{spdymajor}.*

%files -n %{devname}
%doc AUTHORS ChangeLog COPYING NEWS README
%{_includedir}/%{sname}.h
%{_includedir}/microspdy.h
%{_libdir}/%{name}.so
%{_libdir}/libmicrospdy.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/libmicrospdy.pc
%{_datadir}/info/*
%{_mandir}/man3/%{name}.3*
