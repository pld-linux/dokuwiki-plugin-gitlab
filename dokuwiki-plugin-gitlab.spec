%define		subver	2014-11-05
%define		ver		%(echo %{subver} | tr -d -)
%define		plugin		gitlab
%define		php_min_version 5.3.0
%include	/usr/lib/rpm/macros.php
Summary:	GitLab Plugin
Name:		dokuwiki-plugin-%{plugin}
Version:	%{ver}
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/kossmac/dokuwiki-plugin-gitlab/archive/master/%{plugin}-%{subver}.tar.gz
# Source0-md5:	f96c0879cfed610ef1e59cc3c7bbc61e
URL:		https://www.dokuwiki.org/plugin:gitlab
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.553
Requires:	dokuwiki >= 20131208
Requires:	php(core) >= %{php_min_version}
Requires:	php(json)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
Connects to GitLab API an resolves commit hashes to messages

%prep
%setup -qc
mv *-%{plugin}-*/* .

%build
version=$(awk '/^date/{print $2}' plugin.info.txt)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/*.php
%{plugindir}/*.txt
%{plugindir}/conf
