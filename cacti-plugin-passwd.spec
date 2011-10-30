%define		plugin	passwd
%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	Plugin for Cacti - passwd
Summary(pl.UTF-8):	Wtyczka do Cacti - passwd
Name:		cacti-plugin-passwd
Version:	0.2
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://gilles.boulon.free.fr/passwd/%{plugin}-0.1-modified-%{version}.zip
# Source0-md5:	8c94eefb399b3b904e6c0ba5994d752c
URL:		http://forums.cacti.net/viewtopic.php?t=14751
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	unzip
Requires:	cacti
Requires:	php-common >= 4:%{php_min_version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		plugindir		%{cactidir}/plugins/%{plugin}

%description
Plugin for Cacti - user changing passwords.

%description -l pl.UTF-8
Wtyczka do Cacti - zmiana hasła przez użytkownika.

%prep
%setup -qc

%undos -f php,inc
mv %{plugin}/{LICENSE,README} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a %{plugin}/* $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{plugindir}
