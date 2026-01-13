#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	asa
Summary:	asa - Lets your class/object say it works like something else
Name:		perl-asa
Version:	1.04
Release:	2
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/E/ET/ETHER/asa-%{version}.tar.gz
# Source0-md5:	cbe6d1db505eb4eaa2bf35a637fc0451
URL:		https://metacpan.org/release/asa
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl 5 doesn't natively support Java-style interfaces, and it doesn't
support Perl 6 style roles either.

You can get both of these things in half a dozen different ways via
various CPAN modules, but they usually require that you buy into
"their way" of implementing your code.

Other have turned to "duck typing".

This is, for the most part, a fairly naive check that says "can you do
this method", under the "if it looks like a duck, and quacks like a
duck, then it must be a duck".

It assumes that if you have a ->quack method, then they will treat you
as a duck, because doing things like adding Duck to your @ISA array
means you are also forced to take their implementation.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL README
%{perl_vendorlib}/asa.pm
%{_mandir}/man3/asa.3*
