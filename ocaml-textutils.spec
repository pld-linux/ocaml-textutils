#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Text output utilities
Summary(pl.UTF-8):	Narzędzia do wyjścia tekstowego
Name:		ocaml-textutils
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/textutils/tags
Source0:	https://github.com/janestreet/textutils/archive/v%{version}/textutils-%{version}.tar.gz
# Source0-md5:	15b5bba074816c61be6bc0818f1ef402
URL:		https://github.com/janestreet/textutils
BuildRequires:	ocaml >= 1:4.08.0
BuildRequires:	ocaml-core-devel >= 0.14
BuildRequires:	ocaml-core-devel < 0.15
BuildRequires:	ocaml-core_kernel-devel >= 0.14
BuildRequires:	ocaml-core_kernel-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppx_jane-devel >= 0.14
BuildRequires:	ocaml-ppx_jane-devel < 0.15
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
Text output utilities.

This package contains files needed to run bytecode executables using
textutils library.

%description -l pl.UTF-8
Narzędzia do wyjścia tekstowego.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki textutils.

%package devel
Summary:	Text output utilities - development part
Summary(pl.UTF-8):	Narzędzia do wyjścia tekstowego - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-core-devel >= 0.14
Requires:	ocaml-core_kernel-devel >= 0.14
Requires:	ocaml-ppx_jane-devel >= 0.14

%description devel
This package contains files needed to develop OCaml programs using
textutils library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki textutils.

%prep
%setup -q -n textutils-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/textutils/*/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/textutils

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md
%dir %{_libdir}/ocaml/textutils
%{_libdir}/ocaml/textutils/META
%dir %{_libdir}/ocaml/textutils/ascii_table
%{_libdir}/ocaml/textutils/ascii_table/*.cma
%dir %{_libdir}/ocaml/textutils/ascii_table_kernel
%{_libdir}/ocaml/textutils/ascii_table_kernel/*.cma
%dir %{_libdir}/ocaml/textutils/console
%{_libdir}/ocaml/textutils/console/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/textutils/ascii_table/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/textutils/ascii_table_kernel/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/textutils/console/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/textutils/ascii_table/*.cmi
%{_libdir}/ocaml/textutils/ascii_table/*.cmt
%{_libdir}/ocaml/textutils/ascii_table/*.cmti
%{_libdir}/ocaml/textutils/ascii_table/*.mli
%{_libdir}/ocaml/textutils/ascii_table_kernel/*.cmi
%{_libdir}/ocaml/textutils/ascii_table_kernel/*.cmt
%{_libdir}/ocaml/textutils/ascii_table_kernel/*.cmti
%{_libdir}/ocaml/textutils/ascii_table_kernel/*.mli
%{_libdir}/ocaml/textutils/console/*.cmi
%{_libdir}/ocaml/textutils/console/*.cmt
%{_libdir}/ocaml/textutils/console/*.cmti
%{_libdir}/ocaml/textutils/console/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/textutils/ascii_table/ascii_table.a
%{_libdir}/ocaml/textutils/ascii_table/*.cmx
%{_libdir}/ocaml/textutils/ascii_table/*.cmxa
%{_libdir}/ocaml/textutils/ascii_table_kernel/ascii_table_kernel.a
%{_libdir}/ocaml/textutils/ascii_table_kernel/*.cmx
%{_libdir}/ocaml/textutils/ascii_table_kernel/*.cmxa
%{_libdir}/ocaml/textutils/console/console.a
%{_libdir}/ocaml/textutils/console/*.cmx
%{_libdir}/ocaml/textutils/console/*.cmxa
%endif
%{_libdir}/ocaml/textutils/dune-package
%{_libdir}/ocaml/textutils/opam
