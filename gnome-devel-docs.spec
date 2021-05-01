%define url_ver	%(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1

Summary:		GNOME Developer Documentation
Name:			gnome-devel-docs
Version:		40.0
Release:		1
License:		GFDL
Source0:		http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
Group:			Books/Other
Url:			http://developer.gnome.org/
BuildArch:		noarch
BuildRequires:		itstool
BuildRequires:		pkgconfig
BuildRequires:		gnome-doc-utils >= 0.5.6
BuildRequires:		gnome-doc-utils-devel
BuildRequires:		itstool
BuildRequires:		libxml2-utils
BuildRequires:		intltool

%description
This package contains the GNOME Handbook, the GNOME Documentation Style Guide
and an Overview of the GNOME Platform.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%doc NEWS  README AUTHORS
