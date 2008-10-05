%define		plugin	passwd
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - passwd
Summary(pl.UTF-8):	Wtyczka do Cacti - passwd
Name:		cacti-plugin-passwd
Version:	0.2
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://gilles.boulon.free.fr/passwd/%{plugin}-0.1-modified-%{version}.zip
# Source0-md5:	8c94eefb399b3b904e6c0ba5994d752c
URL:		http://forums.cacti.net/about14751.html
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		plugindir		%{cactidir}/plugins/%{plugin}

%description
Plugin for Cacti - user changing passwords.

%description -l pl.UTF-8
Wtyczka do Cacti - zmiana hasła przez użytkownika.

%prep
%setup -q -n %{plugin}

# undos the source
find '(' -name '*.php' -o -name '*.inc' ')' -print0 | xargs -0 sed -i -e 's,\r$,,'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README
%{plugindir}
