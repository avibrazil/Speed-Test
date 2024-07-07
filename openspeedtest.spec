Name: openspeedtest
Summary: HTML5 Network Performance Estimation Tool
Version: 1.5
Release: 1
License: MIT
Group: Networking
Source: %{name}.tar.gz
BuildRoot: %{_tmppath}/build-root-%{name}
BuildArch: noarch
Requires: httpd
Packager: Avi Alkalay <avi unix sh>
Url: https://github.com/avibrazil/Speed-Test

%description
Turn your HTTP server into a network speed testing system. Install this static
files, point your browser to http://YOUR-IP/speedtest and check your private
network speed between 2 points of your control.

%prep
%setup -q -n %{name}

%build

%install
mkdir -p %{buildroot}/%{_datadir}/%{name}

# Static HTML5 files
cp -R --preserve=timestamps assets *html %{buildroot}/%{_datadir}/%{name}/

# Apache configuration
install -Dpm 0644 %{name}.conf %{buildroot}/%{_sysconfdir}/httpd/conf.d/%{name}.conf


%post
# Static files used to measure transfer speed
truncate -s 30M %{_datadir}/%{name}/downloading
touch %{_datadir}/%{name}/upload


%files
%{!?_licensedir:%global license %%doc}
%license License.md
%doc README.md
%{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%ghost %{_datadir}/%{name}/downloading
%ghost %{_datadir}/%{name}/upload


%changelog
* Sun Jul 07 2024 Avi Alkalay <avi unix sh> - 1.5-1
- First packaging attempt

