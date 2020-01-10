Name: hunspell-ti
Summary: Tigrigna hunspell dictionaries
%define upstreamid 20090911
Version: 0.%{upstreamid}
Release: 5%{?dist}
Source: http://www.cs.ru.nl/~biniam/geez/dict/ti_ER.zip
Group: Applications/Text
URL: http://www.cs.ru.nl/~biniam/geez/index.php
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPL+
BuildArch: noarch

Requires: hunspell

%description
Tigrigna hunspell dictionaries.

%prep
%setup -q -c

%build
tr -d '\r' < README.txt > README.txt.new
touch -r README.txt README.txt.new
mv -f README.txt.new README.txt

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p ti_ER.* $RPM_BUILD_ROOT/%{_datadir}/myspell/
pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
ti_ER_aliases="ti_ET"
for lang in $ti_ER_aliases; do
        ln -s ti_ER.aff $lang.aff
        ln -s ti_ER.dic $lang.dic
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.txt
%{_datadir}/myspell/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090911-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090911-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090911-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090911-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep 11 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090911-1
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090704-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 06 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090704-1
- initial version
