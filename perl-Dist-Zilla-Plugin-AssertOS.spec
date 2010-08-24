%define upstream_name    Dist-Zilla-Plugin-AssertOS
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Require that our distribution is running on a particular OS
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Data::Compare)
BuildRequires: perl(Devel::CheckOS)
BuildRequires: perl(Dist::Zilla)
BuildRequires: perl(Dist::Zilla::Role::MetaProvider)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Dist::Zilla::Plugin::AssertOS is a the Dist::Zilla manpage plugin that
integrates the Devel::AssertOS manpage so that CPAN authors may easily
stipulate which particular OS environments their distributions may be built
and installed on.

The author specifies which OS or OS families are supported. The necessary
the Devel::AssertOS manpage files are copied to the 'inc/' directory and
'Makefile.PL' is mungled to include the necessary incantation.

On the module user side, the bundled 'inc/' the Devel::AssertOS manpage
determines whether the current environment is supported or not and will die
accordingly.

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
%doc META.yml LICENSE README META.json Changes
%{_mandir}/man3/*
%perl_vendorlib/*


