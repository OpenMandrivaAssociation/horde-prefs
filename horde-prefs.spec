%define prj Horde_Prefs

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-prefs
Version:       0.0.3
Release:       %mkrel 3
Summary:       Horde Prefs package
License:       LGPL
Group:         Networking/Mail
Url:           http://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(pre): php-pear
Requires:      horde-util
Requires:      horde-framework
Requires:      php-pear
Requires:      php-gettext
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde


%description
The Prefs:: class provides a common abstracted interface into the various
preferences storage mediums. It also includes all of the functions for
retrieving, storing, and checking preference values.

%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Horde/Prefs
%{peardir}/Horde/Prefs.php
%{peardir}/Horde/Prefs/CategoryManager.php
%{peardir}/Horde/Prefs/UI.php
%{peardir}/Horde/Prefs/imsp.php
%{peardir}/Horde/Prefs/kolab.php
%{peardir}/Horde/Prefs/ldap.php
%{peardir}/Horde/Prefs/session.php
%{peardir}/Horde/Prefs/sql.php



%changelog
* Sat Jul 31 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.3-3mdv2011.0
+ Revision: 564080
- Increased release for rebuild

* Wed Mar 17 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.3-2mdv2010.1
+ Revision: 523035
- replaced Requires(pre): %%{_bindir}/pear with Requires(pre): php-pear
  increased release version

* Mon Feb 22 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.3-1mdv2010.1
+ Revision: 509383
- removed Buildrequires: horde-framework
- replaced PreReq with Requires(pre)
- Initial import


