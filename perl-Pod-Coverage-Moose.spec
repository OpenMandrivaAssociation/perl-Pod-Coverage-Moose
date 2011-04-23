%define upstream_name    Pod-Coverage-Moose
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    L<Pod::Coverage> extension for L<Moose>
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Class::MOP)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(FindBin)
BuildRequires: perl(Moose)
BuildRequires: perl(Perl6::Junction)
BuildRequires: perl(Pod::Coverage)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)
BuildRequires: perl(namespace::clean)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


