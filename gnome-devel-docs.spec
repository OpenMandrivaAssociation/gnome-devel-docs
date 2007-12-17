Summary: GNOME Developer Documentation
Name: gnome-devel-docs
Version: 2.20.0
Release: %mkrel 1
License: GPL
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Group: Books/Other
Url: http://www.gnome.org/
BuildArch: noarch
BuildRequires: scrollkeeper pkgconfig
BuildRequires: gnome-doc-utils >= 0.5.6
Requires(post): scrollkeeper >= 0.3
Requires(postun): scrollkeeper >= 0.3

%description
This package contains the GNOME Handbook, the GNOME Documentation Style Guide
and an Overview of the GNOME Platform.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome --all-name
rm -rf %buildroot/var/lib/scrollkeeper
for omf in %buildroot%_datadir/omf/*/*-??*.omf;do 
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name.lang
done

%clean 
rm -rf $RPM_BUILD_ROOT

%post
%update_scrollkeeper

%postun
%clean_scrollkeeper

%files -f %{name}.lang
%defattr(-, root, root)
%doc NEWS  README AUTHORS
%dir %{_datadir}/omf/*
%{_datadir}/omf/*/*-C.omf


