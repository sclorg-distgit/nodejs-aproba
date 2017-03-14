%{?scl:%scl_package nodejs-aproba}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global packagename aproba

# Tests are disabled until nodejs-tap is updated
%global enable_tests 0

Name:		%{?scl_prefix}nodejs-aproba
Version:	1.0.4
Release:	2%{?dist}
Summary:	Function argument validator

License:	MIT and CC-BY
URL:		https://github.com/iarna/aproba
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz

ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	%{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
# BuildRequres for tests go here
%endif

%description
A ridiculously light-weight function argument validator

%prep
%setup -q -n package

%build
# Nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
#%{__nodejs} -e 'require("./")'

%if 0%{?enable_tests}
# test suite goes here
/usr/bin/tap test/*.js
%endif

%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Fri Sep 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.4-2
- Built for RHSCL

* Wed Jul 20 2016 Stephen Gallagher <sgallagh@redhat.com> - 1.0.4-1
- Update to latest upstream release 1.0.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Stephen Gallagher <sgallagh@redhat.com> - 1.0.1-1
- Initial packaging
