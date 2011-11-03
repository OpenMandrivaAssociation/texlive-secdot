# revision 20208
# category Package
# catalog-ctan /macros/latex/contrib/secdot
# catalog-date 2010-10-17 10:06:32 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-secdot
Version:	1.0
Release:	1
Summary:	Section numbers with trailing dots
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/secdot
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/secdot.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/secdot.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Makes the numbers of \section commands come out with a trailing
dot. Includes a command whereby the same can be made to happen
with other sectioning commands.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/secdot/secdot.sty
%doc %{_texmfdistdir}/doc/latex/secdot/secdot.ltx
%doc %{_texmfdistdir}/doc/latex/secdot/secdot.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
