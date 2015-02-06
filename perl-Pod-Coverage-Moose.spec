%define upstream_name    Pod-Coverage-Moose
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	L<Pod::Coverage> extension for L<Moose>
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Pod/Pod-Coverage-Moose-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(namespace::autoclean)
BuildRequires: perl(Test::Requires)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Class::MOP)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Perl6::Junction)
BuildRequires:	perl(Pod::Coverage)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
BuildRequires:	perl(namespace::clean)
BuildArch:	noarch

%description
When using the Pod::Coverage manpage in combination with the Moose manpage,
it will report any method imported from a Role. This is especially bad when
used in combination with the Test::Pod::Coverage manpage, since it takes
away its ease of use.

To use this module in combination with the Test::Pod::Coverage manpage, use
something like this:

  use Test::Pod::Coverage;
  all_pod_coverage_ok({ coverage_class => 'Pod::Coverage::Moose'});

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.20.0-2mdv2011.0
+ Revision: 656822
- rebuild for updated spec-helper

* Wed Aug 25 2010 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2011.0
+ Revision: 573145
- import perl-Pod-Coverage-Moose



