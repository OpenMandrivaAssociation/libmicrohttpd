%define sname microhttpd
%define major 12
%define libname %mklibname %{sname} %major
%define devname %mklibname -d %{sname}

%define _disable_rebuild_configure 1

Summary:	Small C library to run an HTTP server
Name:		libmicrohttpd
Version:	0.9.69
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		http://gnunet.org/libmicrohttpd/
Source0:	http://ftp.gnu.org/gnu/libmicrohttpd/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	gettext-devel

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
Provides:	%{mklibname microspdy 0} = 0.9.47
Obsoletes:	%{mklibname microspdy 0} < 0.9.47
Obsoletes:	microspdy2http < 0.9.47

%description -n %{libname}
libmicrohttpd is a small C library that is supposed to make it easy to
run an HTTP server as part of another application.

%package -n %{devname}
Summary:	Development files for %{libname}
Group:		System/Libraries
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Provides:	%{mklibname microspdy -d} = 0.9.47
Obsoletes:	%{mklibname microspdy -d} < 0.9.47

%description -n %{devname}
Development files for %{libname}.

%prep
%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

%files -n %{devname}
%doc AUTHORS NEWS README
%{_includedir}/%{sname}.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/info/*
%{_mandir}/man3/%{name}.3*
