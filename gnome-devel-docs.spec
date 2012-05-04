%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:		GNOME Developer Documentation
Name:			gnome-devel-docs
Version:		3.4.1
Release:		%mkrel 1
License:		GFDL
Source0:		http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
Group:			Books/Other
Url:			http://developer.gnome.org/
BuildArch:		noarch
BuildRequires:		scrollkeeper
BuildRequires:		pkgconfig
BuildRequires:		gnome-doc-utils >= 0.5.6
Requires(post):		scrollkeeper >= 0.3
Requires(postun):	scrollkeeper >= 0.3

%description
This package contains the GNOME Handbook, the GNOME Documentation Style Guide
and an Overview of the GNOME Platform.

%prep
%setup -q

%build
%configure2_5x
#gw broken in 2.28.1
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome --all-name
rm -rf %buildroot/var/lib/scrollkeeper

%files -f %{name}.lang
%doc NEWS  README AUTHORS
