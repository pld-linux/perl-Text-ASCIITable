#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Text
%define	pnam	ASCIITable
Summary:	Text::ASCIITable - Create a nice formatted table using ASCII characters
Summary(pl.UTF-8):	Text::ASCIITable - tworzenie ładne sformatowanych tabel przy użyciu znaków ASCII
Name:		perl-Text-ASCIITable
Version:	0.22
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Text/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6c34e6ed4575d59e8a51cbd4341e85f2
URL:		https://metacpan.org/release/Text-ASCIITable
BuildRequires:	perl-Module-Build >= 0.38
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::ASCIITable is a module creates a nice formatted table using
ASCII characters.

Pretty nifty if you want to output dynamic text to your console or
other fixed-size-font displays, and at the same time it will display
it in a nice human-readable, or "cool" way.

%description -l pl.UTF-8
Text::ASCIITable to moduł tworzący ładne sformatowane tabele przy
użyciu znaków ASCII.

Jest to przydatne kiedy chcemy stworzyć dynamiczny tekst na terminalu
albo innym wyjściu z fontem o stałej szerokości, jednocześnie
wyglądający ładnie i czytelnie dla człowieka.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	--installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install \
	--destdir=$RPM_BUILD_ROOT \
	--create_packlist=0

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Text/*.pm
%{perl_vendorlib}/Text/ASCIITable
%{_mandir}/man3/*
